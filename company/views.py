from django.shortcuts import render
# from django.http import HttpResponse
from .models import branches


# Create your views here.
def Branches(request):
    b = branches.objects.all()
    return render(request,'branches.html',{'branches':b})