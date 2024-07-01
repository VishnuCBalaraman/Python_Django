from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_index(request):
    return render(request,'index.html')

def show_about(request):
    return render(request,'about.html')
    
def show_doctors(request):
    return render(request,'doctors.html')

def show_booking(request):
    return render(request,'booking.html')

def show_contact(request):
    return render(request,'contact.html')

def show_department(request):
    return render(request,'department.html')