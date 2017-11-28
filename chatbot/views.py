from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm,LoginForm

#This is the homepage of my webapp
class HomeView(generic.TemplateView):
    template_name = 'home/index.html'


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')

@login_required
def logoutView(request):
    logout(request)
    messages.success(request,"you are logged out ,please come back soon")  
    return HttpResponseRedirect(reverse_lazy("home"))

class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy("home")
    template_name = "accounts/login.html"
    def form_valid(self, form):
        #colllect the username data from form
        username = form.cleaned_data["username"]
        #collect the password data from form
        password = form.cleaned_data["password"]
        #lets authenticate the user
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active:
            login(self.request,user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)






