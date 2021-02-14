from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Mywebsite/index.html")

def about(request):
    return render(request, "Mywebsite/about.html")

def contact(request):
    return render(request, "Mywebsite/contact.html")




