from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html',{'name': 'Django'})

def add(request):
    a = int(request.POST['num1'])
    b = int(request.POST['num2'])
    c = a + b
    return render(request, 'result.html', {'result': c})
# Create your views here.
