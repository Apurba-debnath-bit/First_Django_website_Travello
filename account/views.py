from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
def register(request):
    if request.method == 'POST':     
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        Password1 = request.POST['password1']
        Password2 = request.POST['password2']

        if Password1 == Password2:
            if User.objects.filter(username = username):
                messages.info(request,'Ooop!! User name is already exists, Please try another')
                return redirect('register')
            elif User.objects.filter(email = email):
                messages.info(request,'Ooop!! Email address is already exists, Please try another')
                return redirect('register')
            else:
                users = User.objects.create_user(username=username, first_name= first_name,last_name=last_name, email=email, password=Password1)
                users.save()
                print('user created')
                return redirect('login') 
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

#logout function:
def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
