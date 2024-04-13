# from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login

# # Create your views here.
# def HomePage(request):
#     return render (request,'home.html')
    

# def SignupPage(request):
#     if request.method=='POST':
#         name=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')
#         if pass1!=pass2:
#             return HttpResponse("Your password and confirm password are not matched!")
#         else:
#             my_User=User.objects.create_user(name,email,pass1,)
#             my_User.save()

#             # print(name,email,pass1,pass2)
#             return redirect('login')

#             # return HttpResponse('User has been Created successfully')
#             # return redirect('login')
       

#         # print(username,email,password1,password2)
#     return render (request,'registration.html')

# def LoginPage(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         pass1=request.POST.get('password')
#         user=authenticate(request,username=username,password=pass1)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
#     else:
#         return render(request, 'login.html')

#         # print(username,pass1)
#     # return render (request,'login.html')
    


from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError  # Import IntegrityError

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not matched!")
        else:
            try:
                my_User = User.objects.create_user(name, email, pass1)
                my_User.save()
                return redirect('login')
            except IntegrityError:  # Handle IntegrityError
                error_message = "Username already exists. Please choose a different username."
                return render(request, 'registration.html', {'error_message': error_message})
    return render(request, 'registration.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    





