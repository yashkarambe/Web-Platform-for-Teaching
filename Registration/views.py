from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import log_in_registtration
from django.views.decorators.csrf import requires_csrf_token





def index(request):
    # print('app running')
    return render(request , 'Registration/index.html')

@requires_csrf_token
def login_data(request):
    if request.method == 'POST':
        post = log_in_registtration()
        post.Email = request.POST.get("Email")
        post.account_type = request.POST.get('account_type')
       
        password = request.POST.get('pass' )
        repassword = request.POST.get('repass' )
        if password == repassword:
            post.password = request.POST.get('pass' )
            print(password)
            post.save()
            return render(request , 'Registration/index.html')   
        else:
            return HttpResponse("Password do not match ! please recheck again.")
        # print(Email,password,acount_type)
        
    