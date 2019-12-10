from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('register/',views.signup,name='user_register'),
    url('auth/', auth_views.LoginView.as_view(template_name='loginw3school.html'), name='login'),

]
