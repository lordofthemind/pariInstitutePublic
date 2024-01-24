from django.shortcuts import render
from django.http import HttpResponse
from superuser.models import *


# Create your views here.


def landing(request):
    superuser = Superuser.objects.all()[::-1][:1]
    studentc = Student.objects.all().count()
    coursec = Course.objects.all().count()
    facultyc = Faculty.objects.all().count()
    faculty = Faculty.objects.all()[::-1][:3]
    course = Course.objects.all()[::-1][:6]
    return render(
        request,
        "landing/index.html",
        {
            "course": course,
            "superuser": superuser,
            "studentc": studentc,
            "coursec": coursec,
            "facultyc": facultyc,
            "faculty": faculty,
        },
    )


def courseDetail(request, pk):
    course = Course.objects.get(id=pk)
    learn = CrsLrn.objects.filter(course=course)[::-1]
    return render(
        request, "landing/courseDetail.html", {"course": course, "learn": learn}
    )


def pricing(request):
    return HttpResponse("<h1>Pricing</h1>")
    # return render(request, 'landing/pricing.html')


def error404(request, exception):
    return render(request, "landing/page-error-404.html")


def error403(request, exception):
    return render(request, "landing/page-error-403.html")


def error500(request):
    return render(request, "landing/page-error-500.html")
