from django import forms
from .models import Class , Student
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()

#A login form 
class LoginForm(forms.Form):
    
    your_id = forms.CharField(label="Your id ")
    your_pass = forms.CharField(label="Your pass",
    widget=forms.PasswordInput,min_length=8)

    def clean(self):
        your_id = self.cleaned_data["your_id"]
        your_pass = self.cleaned_data["your_pass"]
        user = authenticate(username=your_id,password=your_pass)
        
        if not user:
            raise forms.ValidationError("User doesnt exist")
        
        if not user.check_password(your_pass):
            raise forms.ValidationError("Incorrect Password")

        
        return super(LoginForm,self).clean()





#A registration Form
class StudentForm(forms.ModelForm):
# Clean method which checks whether password matches or not
#and returns the cleaned data and put it in the register form 
## view    
    #Model form
    class Meta:
        model = Student
        fields = ["Rollno","Password","Semester"]
        #exclude = ("Semester",)
     

class Class(forms.ModelForm):
    
    class Meta:
        model = Class
        fields =["Dob","Name","Sem"]