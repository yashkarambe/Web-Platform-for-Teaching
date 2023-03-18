from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import log_in_registtration_student
from .models import log_in_registtration_teacher
from django.views.decorators.csrf import requires_csrf_token
from django.contrib import messages   # for Django masseage show
import numpy as np
from django.contrib.auth  import authenticate,  login, logout



def index(request):
    # print('app running')
    return render(request , 'Registration/index.html')


# Singup Form Data insert 
@requires_csrf_token
def login_data(request):
    if request.method == 'POST':
        account_type = request.POST.get('account_type')
        if account_type == 'Student':
            # inseert data in student table
            post = log_in_registtration_student()
        elif account_type == "Teacher" : 
            # insert data into teacher table
            post = log_in_registtration_teacher()
            
        post.User_name = request.POST.get("user")
        post.Email = request.POST.get("Email")
        post.account_type = request.POST.get('account_type')
       
    #--> Check the password And re-entered pass is matching or not.
        password = request.POST.get('pass' )
        repassword = request.POST.get('repass' )
        if password == repassword:
            post.password = request.POST.get('pass' )
            print(password)
            post.save()
            messages.success(request,'Your account has been created.')
            return render(request , 'Registration/index.html')   
        else:
            messages.error(request,'password does not match , Please Re-check your password.')
            return render(request , 'Registration/index.html')   


def login(request):
    pass_match = False
    
    user = request.POST.get('user_login')
    Email = request.POST.get('Email_login')
    password = request.POST.get('log_pass')
    account_type = request.POST.get('account_type_log')
    login_data = {'User_name': user, 'Email': Email, 'password': password, 'account_type': account_type}
    print(login_data)  #-->  for testing 
    
    Data = []
    if account_type == "Student" :
        Data.extend(log_in_registtration_student.objects.values('User_name','Email' , 'password' ,'account_type'))
           
    if account_type == "Teacher" : 
        Data.extend(log_in_registtration_teacher.objects.values('User_name','Email' , 'password' ,'account_type'))
    print(len(Data))
    for i in range(len(Data)):  
            if Data[i] == login_data : 
                print(Data[i]) #--> for testing 
                pass_match = True
                break
        
    if pass_match:
        if account_type == "Student" :
            messages.success(request,f' Wellcome to Educative {user}.')
            return render(request , "Registration/home/index.html")    
           
        if account_type == "Teacher" :
            # return None 
            pass
    else:
        messages.error(request,"OOP's! Invalid password or User name.")
        return render(request , 'Registration/index.html') 

def logout_handeler(request):
    logout(request)
    messages.success(request , " logout Succcess.")
    return render(request , 'Registration/index.html')
