from django.http import HttpResponseRedirect
from django.template import loader
from django.url import reverse
from django.shortcuts import render, redirect
from .forms import StudentForm, Class, LoginForm
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
)
# Create your views here.

def index(request):
    #post request
    if request.method == "POST":

        #create a post instance of the login form 
        form = LoginForm(request.POST)
        
        #Check validation of the form
        if form.is_valid():
            #process data in the clean method
            username = form.cleaned_data["your_id"]
            password = form.cleaned_data["your_pass"]
            user = authenticate(username=username,password=password)
            login(request, user)



            #my template 
            return HttpResponseRedirect()

    else:

        form = LoginForm()




    return render(request,'index.html',{'form':form})

def register(request):
    #Check for the post request
    if request.method == 'POST':
        #instance of register_form created having Post request
        student_form = StudentForm(request.POST)
        class_form = Class(request.POST)
        
        #if the form is validate
        if student_form.is_valid() and class_form.is_valid():

            #process the data in form.cleaned_data as required
            print(student_form.clean())

            #save the data in the student model
            student_form.save()

            #save the data of form in the class model
            class_form.save()

            #render other page 
            return HttpResponseRedirect('/register_done')
    else:
        #if no post request then form is blank
        class_form = Class()
        student_form = StudentForm()


    return render(request,'register.html',{'class_form':class_form,
    'student_form':student_form})


