from django.shortcuts import render
# from django.http import HttpResponse
from .models import branches
from .forms import newDepartmentToBrancheForm


# Create your views here.
def Branches(request):
    b = branches.objects.all()
    return render(request,'company/branches.html',{'branches':b})

def BrancheDetails(request,branche_id):
    b= branches.objects.get(pk=branche_id)
    return render(request,'company/brancheDetails.html',{'branche':b})

def newBranche(request):
    if request.method == 'POST':
        name = request.POST['brancheName']
        address = request.POST['brancheAddress']
        phone = request.POST['branchePhone']
        email = request.POST['brancheEmail']
        branches.objects.create(
            name= name,address= address,phone= phone,email=email
        )

    return render(request,'company/newBranche.html')

def newDepartmentToBranche(request,branche_id):
    b = branches.objects.get(pk=branche_id)
    form = newDepartmentToBrancheForm()
    if request.method == 'POST':
        form = newDepartmentToBrancheForm(request.POST)
        department = form.save(commit=False)
        department.branch_id = branche_id
        if department.is_valid():
            department = form.save(commit=False)
            department.branch_id = branche_id
            department.save()
            return render(request,'company/brancheDetails.html',{'branche':b})
    # print(form)
    # print(form.fields)
    return render(request,'company/newDepartmentToBranche.html',{'form':form,'branche':b})
    

