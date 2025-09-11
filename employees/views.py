from django.shortcuts import get_object_or_404 
from django.shortcuts import render
from .models import Employee

# from django.http import HttpResponse


# Create your views here.

def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    context={
        "employee":employee,
    }
    return render(request ,'employee_detail.html',context)
    
    
   

