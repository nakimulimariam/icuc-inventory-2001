from django.shortcuts import render

def home_view(request):
    return render(request,'home.html')
def aboutus_view(request):
    return render(request,'aboutus.html')
def gallery_view(request):
    return render(request,'gallery.html')
def services_view(request):
    return render(request,'services.html')
def contactus_view(request):
    return render(request,'contactus.html')


