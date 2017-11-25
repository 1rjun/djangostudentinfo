from django import forms
from .models import Class , Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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


class StudentRegistration(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    birthday = forms.DateField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def save(self,commit=True)
    user = super(StudentRegistration,self).save(commit=False)
