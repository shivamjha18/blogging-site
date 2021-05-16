from django.shortcuts import render
from app.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'contact.html')

def eng(request):
    return render(request,'eng.html')
def cpp(request):
    return render(request,'cpp.html')
def dsa(request):
    return render(request,'dsa.html')


