from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from superuser.models import *
from django.core.mail import send_mail
import string, random

# Create your views here.
def f_login(request):
    try:
        Faculty.objects.get(email=request.session['femail'])
        return redirect('f_dashboard')
    except:
        if request.method == 'POST':
            try:
                fid = Faculty.objects.get(email=request.POST['email'])
                if fid.is_active == True:
                    if fid.password == request.POST['password']:
                        request.session['femail'] = request.POST['email']
                        return redirect('f_dashboard')
                    else:
                        msg = 'Invalid Email or Password'
                        return render(request, 'faculty/f_login.html',{'rmsg':msg})
                else:
                    msg = 'Account is Inactive Please Contact Institute'
                    return render(request, 'faculty/f_login.html',{'rmsg':msg})
            except:
                msg = 'Invalid Email or Password'
                return render(request, 'faculty/f_login.html',{'rmsg':msg})
        else:
            return render(request, 'faculty/f_login.html')


def f_logout(request):
    try:
        del request.session['femail']
    except:
        pass
    return redirect('f_login')


def f_frgtpswd(request):
    if request.method == 'POST':
        try:
            fid = Faculty.objects.get(email=request.POST['email'])
            characters = string.ascii_letters + string.digits + string.punctuation
            PSWORD = ''.join(random.choices(characters,k=10))
            fid.password = PSWORD
            fid.save()
            msg = 'Your New faculty Password is : '+PSWORD
            send_mail(
                'New Faculty Password',
                msg,
                settings.EMAIL_HOST_USER,
                [fid.email],
                fail_silently=False,
            )
            msg = 'Check Your  Email'
            return render(request, 'faculty/f_forgotpswd.html',{'gmsg':msg})
        except:
            msg = 'Invalid Email'
            return render(request, 'faculty/f_forgotpswd.html',{'rmsg':msg})
    return render(request, 'faculty/f_forgotpswd.html')


def f_dashboard(request):
    fid = Faculty.objects.get(email=request.session['femail'])
    return render(request, 'faculty/f_dashboard.html',{'fid':fid})


def f_profileUpdate(request):
    fid = Faculty.objects.get(email=request.session['femail'])
    return render(request, 'faculty/f_profile.html',{'fid':fid})


def f_assindBatches(request):
    fid = Faculty.objects.get(email=request.session['femail'])
    asindbatch = Batch.objects.filter(faculty = fid)
    return render(request, 'faculty/f_batches.html',{'fid':fid,'asindbatch':asindbatch})
    

def f_assingment(request):
    fid = Faculty.objects.get(email=request.session['femail'])
    return render(request, 'faculty/f_assingment.html',{'fid':fid})


def f_notes(request):
    fid = Faculty.objects.get(email=request.session['femail'])
    return render(request, 'faculty/f_notes.html',{'fid':fid})



