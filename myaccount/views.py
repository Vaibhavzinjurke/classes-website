from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from student.models import details

# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            request.session['username']=username
            request.session['password']=password
            
            return redirect('dashboard')
        else:
            return redirect('login')
        
    return render(request,'myaccount/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

    
@login_required(login_url='/myaccount/login')
def dashboard(request):
    
    username=request.session['username']
    data=details.objects.all()
    context={
        "username" : username,
        "data" : data,
    }
    return render (request,"myaccount/dashboard.html",context)

def single_student_record(request, id ):
    data=details.objects.get(id=id)
    context={
        'data' :data
    }
    if request.method=='POST':
        name=request.POST.get('name')
        city = request.POST.get('city')
        degree = request.POST.get('degree')
        year = request.POST.get('year')
        email = request.POST.get ('email')
        course = request.POST.get ('course')
        data.name=name
        data.city=city
        data.degree=degree
        data.year=year
        data.email=email
        data.course=course
        data.save()
        return redirect('dashboard')
        
        
    return render (request, 'myaccount/single_student_records.html', context)

def delete (request,id):
    data=details.objects.get(id=id)
    data.delete()
    return redirect('dashboard')