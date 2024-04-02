from django.shortcuts import redirect, render


from student.models import Placement, details
from django.contrib.auth.decorators import login_required

# Create your views here.

def home (request):
            return render(request,'student/home.html')
        
def about (request):
            return render(request,'student/about.html')
        
def registration (request):
    if request.method=='POST':
        name=request.POST.get('name')
        city = request.POST.get('city')
        degree = request.POST.get('degree')
        year = request.POST.get('year')
        email = request.POST.get ('email')
        course = request.POST.get ('course')
        data= details(name=name,city=city,degree=degree, year=year,email=email,course=course)
        data.save()
        return redirect ("/")
        
    
    return render(request,'student/registration.html')
        
def placement (request):
    placed_student_data=Placement.objects.all()
    context={
        'data':placed_student_data
    }
    
    return render(request,'student/placement.html',context)

        
def python (request):
            return render(request,'student/python.html')
        
def java (request):
            return render(request,'student/java.html')
        
def aws (request):
            return render(request,'student/aws.html')