from.models import student
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    
    return render(request,"home.html")


def list_all_student (request):
    from.models import student
    students=student.objects.all()     #we use filter in place of all to find out paticular students list
    context={
        
        "students":students
        
    }
    return render(request,"table.html",context=context)

def register(request): 
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        roll_no=request.POST['roll_no']
        bio=request.POST['bio']
        obj=student()
        obj.name=name
        obj.email=email
        obj.roll_no=roll_no
        obj.bio=bio
        obj.save()
        return redirect('/')
        
    return render(request,"form.html") 
    
