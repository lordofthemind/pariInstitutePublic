from django.shortcuts import render, redirect
from .models import *
from faculty.models import *
from student.models import *
from django.conf import settings
from django.core.mail import send_mail
import string, random


# Create your views here.
def s_login(request):
    try:
        Superuser.objects.get(email=request.session["suemail"])
        return redirect("s_dashboard")
    except:
        if request.method == "POST":
            try:
                suid = Superuser.objects.get(email=request.POST["email"])
                if suid.password == request.POST["password"]:
                    request.session["suemail"] = request.POST["email"]
                    return redirect("s_dashboard")
                else:
                    msg = "Invalid Email or Password"
                    return render(request, "superuser/s_login.html", {"rmsg": msg})
            except:
                msg = "Invalid Email or Password"
                return render(request, "superuser/s_login.html", {"rmsg": msg})
        else:
            return render(request, "superuser/s_login.html")


def s_logout(request):
    try:
        del request.session["suemail"]  # Deletes session
    except:
        pass
    return redirect("s_login")  # returns login page


def s_frgtpswd(request):
    if request.method == "POST":
        try:
            suid = Superuser.objects.get(email=request.POST["email"])
            characters = string.ascii_letters + string.digits + string.punctuation
            PSWORD = "".join(random.choices(characters, k=10))
            subject = "New password for Superuser Account"
            message = f"""Dear Mr. {suid.last_name},
            Password for your Superuser account has been Updated
            here is your new Password,
            PASSWORD=> {PSWORD}
            You can login with this password and change it later.
            Thank You"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [
                suid.email,
            ]
            send_mail(subject, message, email_from, recipient_list)
            suid.password = PSWORD  # Updates password
            suid.save()  # Saves password
            msg = "Check the email we've sent"
            return render(request, "superuser/s_forgotpswd.html", {"gmsg": msg})
        except:
            msg = "Invalid Email"
            return render(request, "superuser/s_forgotpswd.html", {"rmsg": msg})
    return render(request, "superuser/s_forgotpswd.html")


def s_dashboard(request):
    suid = Superuser.objects.get(email=request.session["suemail"])

    return render(request, "superuser/s_dashboard.html", {"suid": suid})


def s_courses(request):
    suid = Superuser.objects.get(email=request.session["suemail"])
    course = Course.objects.all()[::-1]
    if request.method == "POST":
        try:
            Course.objects.get(name=request.POST["corsname"])
            msg = "Same course name exist already,Try with another."
            course = Course.objects.all()[::-1]
            return render(
                request,
                "superuser/s_courses.html",
                {"course": course, "suid": suid, "rmsg": msg},
            )
        except:
            Course.objects.create(
                name=request.POST["corsname"],
                fee=request.POST["corsfee"],
                duration=request.POST["corsdrsn"],
                lectures=request.POST["lectures"],
                categories=request.POST["catagory"],
                level=request.POST["level"],
                srt_desc=request.POST["corssdesc"],
                lng_desc=request.POST["corsldesc"],
                pic=request.FILES["corspic"],
            )
            msg = "New Course Created Successfully"
            course = Course.objects.all()[::-1]
            return render(
                request,
                "superuser/s_courses.html",
                {"course": course, "suid": suid, "gmsg": msg},
            )
    return render(request, "superuser/s_courses.html", {"course": course, "suid": suid})


def s_addLearn(request):
    suid = Superuser.objects.get(
        email=request.session["suemail"]
    )  # Stores data of Email in variable
    course = Course.objects.all()[::-1]
    if request.method == "POST":
        CrsLrn.objects.create(
            course=Course.objects.get(id=request.POST["corsnm"]),
            lrn_nm=request.POST["corslrnm"],
            lrn_dsc=request.POST["corslrndesc"],
        )
        msg = "Learn Added"
        return render(
            request,
            "superuser/s_courses.html",
            {"course": course, "suid": suid, "gmsg": msg},
        )


def s_courseDetail(request, pk):
    suid = Superuser.objects.get(email=request.session["suemail"])
    course = Course.objects.get(id=pk)
    learn = CrsLrn.objects.filter(course=course)[::-1]
    return render(
        request,
        "superuser/s_courseDetail.html",
        {"course": course, "learn": learn, "suid": suid},
    )


def s_courseActivate(request, pk):
    course = Course.objects.get(id=pk)
    course.is_active = True
    course.save()
    return redirect("s_courses")


def s_courseDeactivate(request, pk):
    course = Course.objects.get(id=pk)
    course.is_active = False
    course.save()
    return redirect("s_courses")


def s_courseDelete(request, pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect("s_courses")


def s_faculty(request):
    suid = Superuser.objects.get(email=request.session["suemail"])
    faculty = Faculty.objects.all()[::-1]
    if request.method == "POST":
        try:
            Faculty.objects.get(email=request.POST["email"])
            msg = "Email is already registered try with another"
            return render(
                request, "superuser/s_faculty.html", {"suid": suid, "rmsg": msg}
            )
        except:
            try:
                Faculty.objects.get(mobile=request.POST["mobile"])
                msg = "Mobile is already registered try with another"
                return render(
                    request, "superuser/s_faculty.html", {"suid": suid, "rmsg": msg}
                )
            except:
                characters = string.ascii_letters + string.digits + string.punctuation
                PSWORD = "".join(random.choices(characters, k=10))
                Faculty.objects.create(
                    fname=request.POST["fname"],
                    lname=request.POST["lname"],
                    mobile=request.POST["mobile"],
                    email=request.POST["email"],
                    password=PSWORD,
                    dob=request.POST["dob"],
                    pic=request.FILES["slfpic"],
                    qualification=request.POST["qualif"],
                    qualf_pic=request.FILES["qualifpic"],
                    experties_1=request.POST["exp1"],
                    experties_2=request.POST["exp2"],
                    doc_type=request.POST["doctype"],
                    address=request.POST["adrss"],
                    doc_num=request.POST["docnum"],
                    doc_pic=request.FILES["docpic"],
                )
                subject = "New Faculty Account Created(credentials)"
                message = f"""Dear Mr. {request.POST['lname']},
                Your new Faculty Account has been created at Pari Computer Classes.
                Now you can login in website in Faculty portal with valid given credentials.
                here is your Password,
                PASSWORD=> {PSWORD}
                You can login with this password and change it later.
                Thank You"""
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [
                    request.POST["email"],
                ]
                send_mail(subject, message, email_from, recipient_list)
                msg = "New faculty created successfully"
                return render(
                    request,
                    "superuser/s_faculty.html",
                    {"suid": suid, "faculty": faculty, "gmsg": msg},
                )
    return render(
        request, "superuser/s_faculty.html", {"suid": suid, "faculty": faculty}
    )


def s_facultyDetail(request, pk):
    suid = Superuser.objects.get(email=request.session["suemail"])
    faculty = Faculty.objects.get(id=pk)
    asindbatch = Batch.objects.filter(faculty=faculty)
    return render(
        request,
        "superuser/s_facultyDetail.html",
        {"suid": suid, "faculty": faculty, "asindbatch": asindbatch},
    )


def s_facultyActivate(request, pk):
    suid = Superuser.objects.get(email=request.session["suemail"])
    faculty = Faculty.objects.get(id=pk)
    faculty.is_active = True
    faculty.save()
    return render(
        request, "superuser/s_facultyDetail.html", {"suid": suid, "faculty": faculty}
    )


def s_facultyDeactivate(request, pk):
    suid = Superuser.objects.get(email=request.session["suemail"])
    faculty = Faculty.objects.get(id=pk)
    faculty.is_active = False
    faculty.save()
    return render(
        request, "superuser/s_facultyDetail.html", {"suid": suid, "faculty": faculty}
    )


def s_facultyDelete(request, pk):
    faculty = Faculty.objects.get(id=pk)
    faculty.delete()
    return redirect("s_faculty")


def s_student(request):
    suid = Superuser.objects.get(email=request.session["suemail"])
    student = Student.objects.all()[::-1]
    return render(
        request, "superuser/s_student.html", {"suid": suid, "student": student}
    )


def s_studentEdit(request, pk):
    suid = Superuser.objects.get(email=request.session["suemail"])
    student = Student.objects.get(id=pk)
    batches = Batch.objects.all()[::-1]
    enrldbatch = Batch.objects.filter(student=student)
    return render(
        request,
        "superuser/s_studentEdit.html",
        {
            "suid": suid,
            "student": student,
            "batches": batches,
            "enrldbatch": enrldbatch,
        },
    )


def s_studentDelete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect("s_student")


def s_studentSearch(request):
    suid = Superuser.objects.get(email=request.session["suemail"])
    student = Student.objects.get()
    return render(
        request, "superuser/s_studentDetails.html", {"suid": suid, "student": student}
    )


def s_studentActivate(request, pk):
    student = Student.objects.get(id=pk)
    student.is_active = True
    student.save()
    return redirect("s_student")


def s_studentDeactivate(request, pk):
    student = Student.objects.get(id=pk)
    student.is_active = False
    student.save()
    return redirect("s_student")


def s_batch(request):
    suid = Superuser.objects.get(
        email=request.session["suemail"]
    )  # Stores data of Email in variable
    course = Course.objects.all()[::-1]
    faculty = Faculty.objects.all()[::-1]
    batches = Batch.objects.all()[::-1]
    if request.method == "POST":
        try:
            Batch.objects.get(timing=request.POST["timing"])
            msg = "Batch timing is not available"
            return render(
                request,
                "superuser/s_batch.html",
                {
                    "suid": suid,
                    "rmsg": msg,
                    "course": course,
                    "faculty": faculty,
                    "batches": batches,
                },
            )
        except:
            Batch.objects.create(
                timing=request.POST["timing"],
                start_dt=request.POST["stdate"],
                course=Course.objects.get(id=request.POST["corsnm"]),
                faculty=Faculty.objects.get(id=request.POST["faculty"]),
            )
            msg = "New Batch Created"
            batches = Batch.objects.all()[::-1]
            return render(
                request,
                "superuser/s_batch.html",
                {
                    "suid": suid,
                    "gmsg": msg,
                    "course": course,
                    "faculty": faculty,
                    "batches": batches,
                },
            )
    return render(
        request,
        "superuser/s_batch.html",
        {"suid": suid, "course": course, "faculty": faculty, "batches": batches},
    )


def s_batchDetail(request, pk):
    suid = Superuser.objects.get(
        email=request.session["suemail"]
    )  # Stores data of Email in variable
    batch = Batch.objects.get(id=pk)
    students = Batch.student.through.objects.all()
    return render(
        request,
        "superuser/s_batchDetail.html",
        {"batch": batch, "suid": suid, "students": students},
    )


def s_batchActivate(request, pk):
    batch = Batch.objects.get(id=pk)
    batch.is_active = True
    batch.save()
    return render(request, "superuser/s_batchDetail.html", {"batch": batch})


def s_batchDeactivate(request, pk):
    batch = Batch.objects.get(id=pk)
    batch.is_active = False
    batch.save()
    return render(request, "superuser/s_batchDetail.html", {"batch": batch})


def s_batchDelete(request, pk):
    batch = Batch.objects.get(id=pk)
    batch.delete()
    return redirect("s_batch")


def s_batchAssign(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        batch = Batch.objects.get(id=request.POST["batch"])
        batch.student.add(student)
        batch.save()
        msg = "Batch Assigned"
        return render(
            request, "superuser/s_studentEdit.html", {"student": student, "gmsg": msg}
        )


def s_profileUpdate(request):
    suid = Superuser.objects.get(
        email=request.session["suemail"]
    )  # Stores data of Email in variable
    dateob = str(suid.dob)
    if request.method == "POST":
        suid.first_name = request.POST["fname"]
        suid.last_name = request.POST["lname"]
        # suid.mobile = request.POST['mobile']
        # suid.email = request.POST['email']
        suid.dob = request.POST["dob"]
        if "slfpic" in request.FILES:
            suid.pic = request.FILES["slfpic"]
        suid.address = request.POST["adrss"]
        suid.about = request.POST["abt"]
        suid.designation = request.POST["dsgntn"]
        suid.occupaion = request.POST["ocupsn"]
        suid.save()
        msg = "Profile updated successfully"
        return render(
            request,
            "superuser/s_profile.html",
            {"suid": suid, "gmsg": msg, "dateob": dateob},
        )
    return render(request, "superuser/s_profile.html", {"suid": suid, "dateob": dateob})


def s_paswrdUpdate(request):
    suid = Superuser.objects.get(email=request.session["suemail"])
    if request.method == "POST":
        if suid.password == request.POST["crntpswd"]:
            if len(request.POST["nwpswd"]) >= 10:
                if request.POST["nwpswd"] == request.POST["cnfnwpswd"]:
                    suid.password = request.POST["nwpswd"]
                    suid.save()
                    msg = "Password Updated Successfully"
                    return render(
                        request, "superuser/s_profile.html", {"suid": suid, "gmsg": msg}
                    )
                else:
                    msg = "Both Passwords Are Not Same"
                    return render(
                        request, "superuser/s_profile.html", {"suid": suid, "rmsg": msg}
                    )
            else:
                msg = "Password Must Be At Least 10 Characters!!!"
                return render(
                    request, "superuser/s_profile.html", {"suid": suid, "rmsg": msg}
                )
        else:
            msg = "Invalid Old Password"
            return render(
                request, "superuser/s_profile.html", {"suid": suid, "rmsg": msg}
            )
    return render(request, "superuser/s_profile.html", {"suid": suid})
