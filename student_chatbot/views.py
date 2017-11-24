from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from .forms import StudentForm, ClassForm, LoginForm
# Create your views here.

def index(request):
    #post request
    if request.method == "POST":

        #create a post instance of the login form 
        form = LoginForm(request.POST)
        
        #Check validation of the form
        if form.is_valid():
            #process data in the clean method
            id=form.clean_your_id()
            print(id)
            
            #my template 
            return redirect('login',data=id)

    else:

        form = LoginForm()




    return render(request,'index.html',{'form':form})

def register(request):
    #Check for the post request
    if request.method == 'POST':
        #instance of register_form created having Post request
        student_form = StudentForm(request.POST)
        class_form = ClassForm(request.POST)
        
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
        register_form = RegisterForm()


    return render(request,'register.html',{'class_form':class_form,
    'student_form':student_form})


def login(request):
    if request.user.is_authenticated:
        data = {
            "text":"Hello i am logeed in"
        }
    else:
        data = {
            "text":"Hello i am logged out "
        }
    return render(request,'login.html',data)


def register_done(request):
    return render(request,'register_done.html')
