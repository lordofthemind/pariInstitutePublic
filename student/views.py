from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from superuser.models import *
from django.core.mail import send_mail
import string, random

# Create your views here.


def st_login(request):
    try:
        Student.objects.get(email=request.session["stemail"])
        return redirect("st_dashboard")
    except:
        if request.method == "POST":
            try:
                stid = Student.objects.get(email=request.POST["email"])
                if stid.is_active == True:
                    if stid.password == request.POST["password"]:
                        request.session["stemail"] = request.POST["email"]
                        return redirect("st_dashboard")
                    else:
                        msg = "Invalid Email or Password"
                        return render(request, "student/st_login.html", {"rmsg": msg})
                else:
                    msg = "Account is Inactive Please Contact Institute"
                    return render(request, "student/st_login.html", {"rmsg": msg})
            except:
                msg = "Invalid Email or Password"
                return render(request, "student/st_login.html", {"rmsg": msg})
        else:
            return render(request, "student/st_login.html")


def st_logout(request):
    try:
        del request.session["stemail"]  # Deletes session
    except:
        pass
    return redirect("st_login")  # returns login page


def st_register(request):
    if request.method == "POST":
        try:
            Student.objects.get(email=request.POST["email"])
            msg = "Email is already registered,Try with another."
            return render(request, "student/st_register.html", {"rmsg": msg})
        except:
            try:
                Student.objects.get(mobile=request.POST["mobile"])
                msg = "Mobile is already registered,Try with another."
                return render(request, "student/st_register.html", {"rmsg": msg})
            except:
                characters = string.ascii_letters + string.digits + string.punctuation
                PSWORD = "".join(random.choices(characters, k=10))
                if "mark12" in request.FILES:
                    Student.objects.create(
                        fname=request.POST["fname"],
                        lname=request.POST["lname"],
                        email=request.POST["email"],
                        fathers_nm=request.POST["fthrname"],
                        mothers_nm=request.POST["mdrname"],
                        password=PSWORD,
                        mobile=request.POST["mobile"],
                        dob=request.POST["dob"],
                        pic=request.FILES["slfpic"],
                        qualification=request.POST["qualif"],
                        address=request.POST["adrss"],
                        mrksht_10th=request.FILES["mark10"],
                        mrksht_12th=request.FILES["mark12"],
                        doc_type=request.POST["doctype"],
                        doc_num=request.POST["docnum"],
                        doc_pic=request.FILES["docpic"],
                        sign_pic=request.FILES["sign"],
                    )
                else:
                    Student.objects.create(
                        fname=request.POST["fname"],
                        lname=request.POST["lname"],
                        email=request.POST["email"],
                        fathers_nm=request.POST["fthrname"],
                        mothers_nm=request.POST["mdrname"],
                        password=PSWORD,
                        mobile=request.POST["mobile"],
                        dob=request.POST["dob"],
                        pic=request.FILES["slfpic"],
                        qualification=request.POST["qualif"],
                        address=request.POST["adrss"],
                        mrksht_10th=request.FILES["mark10"],
                        doc_type=request.POST["doctype"],
                        doc_num=request.POST["docnum"],
                        doc_pic=request.FILES["docpic"],
                        sign_pic=request.FILES["sign"],
                    )
                subject = "New Student Account Requested"
                message = f"""Dear Mr. {request.POST['lname']},
                                Your registration at Pari computer classes is sent for approval.
                                we request you to wait. We will get back to you soon.
                                Your login details are:
                                Email: {request.POST['email']}
                                Password: {PSWORD}
                                Thank You."""
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [
                    request.POST["email"],
                ]
                send_mail(subject, message, email_from, recipient_list)
                msg = "Account request sent"
                return render(request, "student/st_register.html", {"gmsg": msg})
    return render(request, "student/st_register.html")


def st_frgtpswd(request):
    if request.method == "POST":
        try:
            stid = Student.objects.get(email=request.POST["email"])
            characters = string.ascii_letters + string.digits + string.punctuation
            PSWORD = "".join(random.choices(characters, k=10))
            stid.password = PSWORD  # Updates password
            stid.save()  # Saves password
            subject = "New password for Superuser Account"
            message = f"""Dear Student,
            Password for your Student account has been Updated
            here is your new Password,
            PASSWORD=> {PSWORD}
            You can login with this password and change it later.
            Thank You"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [
                stid.email,
            ]
            send_mail(subject, message, email_from, recipient_list)
            msg = "Check the email we've sent"
            return render(request, "student/st_forgotpswd.html", {"gmsg": msg})
        except:
            msg = "Invalid Email"
            return render(request, "student/st_forgotpswd.html", {"rmsg": msg})
    return render(request, "student/st_forgotpswd.html")


def st_dashboard(request):
    stid = Student.objects.get(email=request.session["stemail"])
    return render(request, "student/st_dashboard.html", {"stid": stid})


def st_assingment(request):
    stid = Student.objects.get(email=request.session["stemail"])
    return render(request, "student/st_assingment.html", {"stid": stid})


def st_certificate(request):
    stid = Student.objects.get(email=request.session["stemail"])
    return render(request, "student/st_certificate.html", {"stid": stid})


def st_profileUpdate(request):
    stid = Student.objects.get(email=request.session["stemail"])
    batch = Batch.objects.filter(student=stid)
    return render(request, "student/st_profile.html", {"stid": stid, "batch": batch})


def st_paswrdUpdate(request):
    stid = Student.objects.get(email=request.session["stemail"])
    if request.method == "POST":
        if stid.password == request.POST["crntpswd"]:
            if len(request.POST["nwpswd"]) >= 10:
                if request.POST["nwpswd"] == request.POST["cnfnwpswd"]:
                    stid.password = request.POST["nwpswd"]
                    stid.save()
                    msg = "Password Updated Successfully"
                    return render(
                        request, "student/st_profile.html", {"stid": stid, "gmsg": msg}
                    )
                else:
                    msg = "Both Passwords Are Not Same"
                    return render(
                        request, "student/st_profile.html", {"stid": stid, "rmsg": msg}
                    )
            else:
                msg = "Password Must Be At Least 10 Characters!!!"
                return render(
                    request, "student/st_profile.html", {"stid": stid, "rmsg": msg}
                )
        else:
            msg = "Invalid Old Password"
            return render(
                request, "student/st_profile.html", {"stid": stid, "rmsg": msg}
            )
    return render(request, "student/st_profile.html", {"stid": stid})
