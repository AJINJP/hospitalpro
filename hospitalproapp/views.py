from django.shortcuts import render
from .models import Department
from .models import Doctors
from .form import Bookingform

# Create your views here.
def index(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")
def department(request):
    dict_dept={
        'deptkey':Department.objects.all()
    }
    return render(request,"department.html",dict_dept) 
def about(request):
    return render(request,"about.html")
def booking(request):
    if request.method=="POST":
        formdemo=Bookingform(request.POST)
        if formdemo.is_valid():
            formdemo.save()
        return render(request,"confirm.html")
    myform1=Bookingform()
    dict_book={
        'formkey':myform1
    }
    return render(request,"booking.html",dict_book) 
def docters(request):
    dict_docs={
        'dockey':Doctors.objects.all()
    }
    return render(request,"docters.html",dict_docs)
 