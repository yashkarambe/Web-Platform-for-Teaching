from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import log_in_registtration_student
from .models import log_in_registtration_teacher
from django.views.decorators.csrf import requires_csrf_token
from django.contrib import messages   # for Django masseage show
from django.contrib.auth  import authenticate,  login, logout
from .models import thumnail
from datetime import date
from .models import Playlist
from .models import Quize_thumnail

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
    # print(login_data)  #-->  for testing 
    
    Data = []
    if account_type == "Student" :
        Data.extend(log_in_registtration_student.objects.values('User_name','Email' , 'password' ,'account_type'))
           
    if account_type == "Teacher" : 
        Data.extend(log_in_registtration_teacher.objects.values('User_name','Email' , 'password' ,'account_type'))
    # print(len(Data))
    for i in range(len(Data)):  
            if Data[i] == login_data : 
                # print(Data[i]) #--> for testing 
                pass_match = True
                break
        
    if pass_match:
        if account_type == "Student" :
            messages.success(request,f' Wellcome to Educative {user}.')
            return render(request , "Registration/student/index.html")    
           
        if account_type == "Teacher" :
            messages.success(request ,f' Wellcom to Educative Respected {user}') 
            return render(request , 'Registration/teacher/teacher.html')
    else:
        messages.error(request,"OOP's! Invalid password or User name.")
        return render(request , 'Registration/index.html') 

def logout_handeler(request):
    logout(request)
    messages.success(request , " logout Succcess.")
    return render(request , 'Registration/index.html')

def teacher(request):
    parm = { 'button2' : 'disabled','button1' : 'disabled' }
    return render(request ,"Registration/teacher/teacher.html" , parm)
def quizes(request):
    return render(request ,"Registration/teacher/quizes.html")
def dashboard(request):
    return render(request ,"Registration/teacher/dashboard.html")

@requires_csrf_token
def lecture_authentication(request):
        pass_match = False
        
        user = request.POST.get('user_aut')
        Email = request.POST.get('Email_aut')
        Password = request.POST.get('aut_pass')
        
        authorize = {'User_name': user, 'Email': Email, 'password': Password, 'account_type':'Teacher' }
        # print(authorize)
        Data = []
        Data.extend(log_in_registtration_teacher.objects.values('User_name','Email' , 'password' ,'account_type'))
        
        for i in range(len(Data)):  
            if Data[i] == authorize :
                # print(i) 
                pass_match = True
                break
        
        if pass_match:
            parm ={'button1' : 'active','button' : 'disabled' ,'button2' : 'disabled' }
            return render(request , 'Registration/teacher/teacher.html' , parm)
        
        else:
            parm ={'button2' : 'disabled','button1' : 'disabled'}
            messages.error(request,"OOP's! Invalid password or User name.")
            return render(request , 'Registration/teacher/teacher.html', parm) 
        
        
def thumnail_(request):
    post = thumnail()
    post.playlist_name = request.GET.get('Playlist_Name')
    post.Chapter_name = request.GET.get('Chapter_name')
    post.Topic_name = request.GET.get('Topic_name')
    post.Thumnail_image = request.GET.get('thumnail')
    post.Short_Desc = request.GET.get('Shor_Desc')
    post.pub_date = date.today()
    post.save()
    parm ={'button2' : 'active','button1' : 'disabled' ,'button' : 'disabled' }
    return render(request ,'Registration/teacher/teacher.html', parm) 
     
     
def lectur_Upload(request):
    post = Playlist()
    post.Chapter_name_playlist = request.POST.get('Chapter_name_playlist')
    post.Topic_name_playlist = request.POST.get('Topic_name_playlist')
    post.Leactur_title = request.POST.get('Leactur_title')
    post.Desc_leactur = request.POST.get('Desc_leactur')
    post.Upload_leactur = request.POST.get('Upload_leactur')
    post.save()
    parm ={'button2' : 'active','button1' : 'disabled' ,'button' : 'disabled' }
    messages.success(request , "Uplode all remaining lecture with same chapter and topic name.")
    return render(request , 'Registration/teacher/teacher.html', parm)


def Quize_thum(request):
    Quize_name = request.POST.get('Quize_name')
    chaptr_name = request.POST.get('Chapter_name')
    topic_name = request.POST.get('Topic_name')
    pass_match = False
    check = {"Quize_name":Quize_name,"chaptr_name":chaptr_name,"topic_name":topic_name}
    print(check)
    data=[]
    data.extend(Quize_thumnail.objects.values('Quize_name','chaptr_name','topic_name'))
    for i in range(len(data)):
        if data[i]==check:
            pass_match = True
    if pass_match:
        messages.success(request , "This Quize is already exist! If you want to add Question Uplode all remaining question with same chapter and topic name.")
        parm = {'button1':'active','button2' : 'disabled'}
        return render(request , 'Registration/teacher/quizes.html', parm)
    else: 
        post = Quize_thumnail()
        post.Quize_name = request.POST.get('Quize_name')
        post.chaptr_name = request.POST.get('Chapter_name')
        post.topic_name = request.POST.get('Topic_name')
        post.thumnail = request.POST.get('thumnail')
        post.marks_per_que = request.POST.get('Marks_per_Que')
        post.descreption = request.POST.get('Description')
        post.save()
        print('success')    
        parm = {'button1':'active','button2' : 'disabled'}
        messages.success(request , "Uplode all remaining question with same chapter and topic name.")
        return render(request , 'Registration/teacher/quizes.html', parm)
    