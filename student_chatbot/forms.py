from django import forms
from .models import Class , Student
#A login form 
class LoginForm(forms.Form):
    
    your_id = forms.IntegerField(label="Your id ")
    your_pass = forms.CharField(label="Your pass",
    widget=forms.PasswordInput,min_length=8)

    def clean_your_id(self):
        your_id = self.cleaned_data["your_id"]
        return your_id


#A registration Form
class RegisterForm(forms.ModelForm):

    Rollno = forms.IntegerField(label="Rollno")
    Name = forms.CharField(label="Name")
    Class = forms.CharField(label="Semester")
    Dob = forms.DateTimeField(label="Dob")
    Password = forms.CharField(label="Password",
    widget=forms.PasswordInput,min_length=8)
    Re_Password=forms.CharField(label="Confirm-Password",
    widget=forms.PasswordInput,min_length=8)

# Clean method which checks whether password matches or not
#and returns the cleaned data and put it in the register form 
## view
    def clean(self):

        #it will call the RegisterForm and clean its values
        #and save in a variable
        cleaned_data = super(RegisterForm, self).clean()
        #make the instance of Password 
        Pass = cleaned_data["Password"]
        Re_Pass = cleaned_data["Re_Password"]
        if Pass != Re_Pass:
            raise forms.ValidationError("Password doesn't Match")
        return cleaned_data
    
    class Meta:
        model = Class