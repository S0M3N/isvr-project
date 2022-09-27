from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.
def courses(request):
    return render(request, 'courses.html')

def course(request, slug):
    std = Course.objects.filter(slug = slug)[0]
    return render(request, 'course_info.htm', {'std':std})

def apply(request):
    if request.method == "POST":
        try:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            contact = request.POST['contact']
            course = request.POST['course']
            month = request.POST['month']
            if fname=="" or lname == "" or email == "" or contact == "":
                messages.error(request,'All fields are Required.') 
            else:
                val = Application(first_name = fname, last_name = lname, email = email, contact = contact, course = course, month = month)
                val.save()
                messages.success(request, 'Form filled successfully we will be with you soon.')
        except:
            messages.error(request, "Cannot apply right now, please check all fields or please try again later.")
    return render(request, 'course/course_apply.html')