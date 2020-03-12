from django.shortcuts import render

def homeView(request):
    return render(request,"Pages/Home.html")

def contactView(request):
    return render(request,"Pages/Contact.html")

def aboutView(request):
    return render(request,"Pages/About.html")