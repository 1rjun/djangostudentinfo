from student_chatbot import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^register$',views.register,name='register'),
    url(r'^login$',views.login,name="login"),
    url(r'^register_done',views.login,name="register_done")
]
