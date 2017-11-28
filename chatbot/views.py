from django.views import generic
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy

from .forms import RegistrationForm

#This is the homepage of my webapp
class HomeView(generic.TemplateView):
    template_name = 'home/index.html'


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')
