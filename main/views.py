from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Render the home page of the portfolio.
    """
    return render(request, "main/home.html") 

def projects(request):
    return render(request, "main/projects.html")

def resume(request):
    return render(request, "main/resume.html")

def contact(request):
    return render(request, "main/contact.html")

def gallery(request):
    return render(request, "main/gallery.html") 