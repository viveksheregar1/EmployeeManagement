from django.shortcuts import render,redirect
from django.contrib import messages
from . models import EmployeeRecord

def index(request):
    return render(request,'index.html')

def addemp(request):
    return render(request,'addemp.html')

def searchemp(request):
    return render(request,'searchemp.html')

def employee(request):
    #add new emp
    if 'save' in request.POST:
        empid=int(request.POST['empid'])
        if EmployeeRecord.objects.filter(empid=empid).exists()==False:
            firstname =request.POST['firstname']
            lastname =request.POST['lastname']
            email =request.POST['email']
            contact =int(request.POST['contact'])
            address =request.POST['address']
            department =request.POST['dept']
            salary =int(request.POST['salary'])
            picture=request.FILES['picture']
            record=EmployeeRecord.objects.create(empid=empid,firstname=firstname,lastname=lastname,email=email,contact=contact,department=department,salary=salary,picture=picture,address=address)
            messages.success(request,"Employee Data Saved")
            return render(request,'viewemp.html',{'record':record})
        else:
            messages.info(request,"Employee ID already exists")
            return redirect('addemp')

    #update emp
    elif 'update' in request.POST:
        empid=int(request.POST['empid'])
        record=EmployeeRecord.objects.get(empid=empid)
        record.firstname =request.POST['firstname']
        record.lastname =request.POST['lastname']
        record.email =request.POST['email']
        record.contact =int(request.POST['contact'])
        record.address =request.POST['address']
        record.department =request.POST['dept']
        record.salary =int(request.POST['salary'])
        record.save()
        messages.success(request,"Employee Data Updated")
        return render(request,'viewemp.html',{'record':record})

    #search and view
    if 'search' in request.POST:
        empid=int(request.POST['empid'])
        record=EmployeeRecord.objects.filter(empid=empid)
        if record.exists():
            return render(request,'viewemp.html',{'record':record.values()[0]})
        else:
            messages.info(request,"Employee ID Not Found")
            return redirect('searchemp')

    #delete
    elif 'delete' in request.POST:
        empid=int(request.POST['empid'])
        record=EmployeeRecord.objects.filter(empid=empid).delete()
        messages.success(request,message="employee with ID:"+str(empid)+" is Deleted")
        return redirect('searchemp')

    #view all records
    else:
        records=EmployeeRecord.objects.raw('select * from Empmanager_EmployeeRecord')
        return render(request,'viewallemp.html',{'records':records})


