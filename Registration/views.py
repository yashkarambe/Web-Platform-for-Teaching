from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import log_in_registtration
from django.views.decorators.csrf import requires_csrf_token
from django.contrib import messages   # for Django masseage show





def index(request):
    # print('app running')
    return render(request , 'Registration/index.html')


@requires_csrf_token
def login_data(request):
    if request.method == 'POST':
        post = log_in_registtration()
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
        # print(Email,password,acount_type)
        
    