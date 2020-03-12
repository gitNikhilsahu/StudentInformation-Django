from django.shortcuts import render

def accountHome(request):
    return render(request, 'Account/AccountHome.html')

def registerView(request):
    return render(request, 'Account/Register.html')

def loginView(request):
    return render(request, 'Account/Login.html')

def studentView(request):
    return render(request, 'Student/StudentHome.html')

def adminView(request):
    return render(request, 'Admin/adminHome.html')

def studentViewProfile(request):
    return render(request, 'Student/StudentViewProfile.html')

def studentUpdateProfile(request):
    return render(request, 'Student/StudentUpdateProfile.html')
