from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here
def Signup(request):
    if request.method == 'POST':
        Uname = request.POST.get('User_name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password') 
        Confirmpassword = request.POST.get('Confirm_password')
        if Password != Confirmpassword:
            messages.info( "Password you have enntered are not same!" )
        else:
            UserCred = User.objects.create_user(Uname,Email,Password)
            return redirect('Login')
    else:
        return render(request,'Signup.html')

def Login(request):
    if request.method == 'POST':
        Uname = request.POST.get('User_name')
        Password = request.POST.get('Password')

        UserCredential = authenticate(username = Uname, password = Password)
        if UserCredential is not None:
            login(request,UserCredential)
            return redirect('Dashboard')
        else:
            return HttpResponse( "Username or password was incorrect." )
    else:
        return render(request,'Login.html')

def Forgot_password(request):
    return render(request,'Forgot_password.html')

def Dashboard(request):
    return render(request, 'Dashboard.html')

def Index(request):
    return render(request, 'Dashboard.html')

def Bariaticsurgery_description(request):
    return render(request, 'Bariaticsurgery_description.html')

def Breastcenter_description(request):
    return render(request, 'Breastcenter_description.html')

def Cancer_description(request):
    return render(request, 'Cancer_description.html')

def Chest_description(request):
    return render(request, 'Chest_description.html')

def Dermotology_description(request):
    return render(request, 'Dermotology_description.html')

def Dentist_description(request):
    return render(request, 'Dentist_description.html')

def Ent_description(request):
    return render(request, 'Ent_description.html')

def Endocrinologyanddiabetes_description(request):
    return render(request, 'Endocrinologyanddiabetes_description.html')

def Appointment_schedulling(request):
    if request.method == "POST":
        Full_name = request.POST.get("Full_name")
        Email = request.POST.get("Email")
        Appointment_purpose = request.POST.get("Appointment_purpose")
        Phone_number = request.POST.get("Phone_number")
        Appoint_department = request.POST.get("Appoint_department")
        Appoint_date = request.POST.get("Appoint_date")
        Appoint_time = request.POST.get("Appoint_time")

        # Save the data into the database
        AppointmentCred = User.objects.create_user(
            Full_name = Full_name,
            Email = Email,
            Appointment_purpose = Appointment_purpose,
            Phone_number = Phone_number,
            Appoint_department = Appoint_department,
            Appoint_date=Appoint_date,
            Appoint_time = Appoint_time
        )

        return redirect('Billing_section') 
    else:
        return render(request, 'Appointment_schedule.html')

def Billing_section(request):
    return render(request, 'Billing_section.html')

def Logout(request):
    logout(request)
    return redirect('Login')