from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee

def home(request):
    # return HttpResponse("<h2>Hello, welcome to the home page!</h2>")    # Simple HTTP response
    employees = Employee.objects.all()  # Fetch all employee records  
    # print(employees)  # Debugging: Print to console  
    context={
        'employees': employees
    }
    return render(request, 'homme.html' , context)  # Render the template

 