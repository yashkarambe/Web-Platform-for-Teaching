from django.http import HttpResponse
from django.shortcuts import render
# from..Registration.models import log_in_registtration

def index(request):
    print("main page")
    return render(request , '/Registration/index.html')

