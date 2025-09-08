from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("<h2>Hello, welcome to the home page!</h2>")    # Simple HTTP response
    
    return render(request, 'homme.html')  # Render the template