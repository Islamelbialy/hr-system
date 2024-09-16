from django.shortcuts import render
# from django.http import HttpResponse
from .models import branches,departments
from .forms import newDepartmentToBrancheForm,editDepartmentToBrancheForm


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
        if form.is_valid():
            if departments.objects.filter(name = form.cleaned_data['name'],branch_id = branche_id).exists():
                form.add_error('name','this department is already exists in this branch')
                return render(request,'company/newDepartmentToBranche.html',{'form':form,'branche':b})

            department = form.save(commit=False)
            department.branch_id = branche_id
            department.save()
            return render(request,'company/brancheDetails.html',{'branche':b})
    # print(form)
    # print(form.fields)
    return render(request,'company/newDepartmentToBranche.html',{'form':form,'branche':b})

def editDepartmentToBranche(request,branche_id,depaertment_id):
    form = editDepartmentToBrancheForm()
    b = branches.objects.get(pk=branche_id)
    dept = departments.objects.get(pk=depaertment_id)
    form.fields['name'].initial = dept.name
    form.fields['description'].initial = dept.description
    if request.method == "POST":
        form = editDepartmentToBrancheForm(request.POST)
        if form.is_valid():
            deptformData = form.save(commit=False)
            dept.name = deptformData.name
            dept.description = deptformData.description
            dept.save()
            return render(request,'company/brancheDetails.html',{'branche':b})
    return render(request,'company/editDepartmentToBranche.html',{'form':form,'branche':b,'dept':dept})
    

