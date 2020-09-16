from django.urls import path
from .views import homepageview, aboutpageview, base, formpageview, register, user_login, user_logout


app_name = 'pages'  

urlpatterns = [

path('', homepageview, name='home'),
path ('about/',aboutpageview, name='about'),
path('base/', base, name='base'),
path('formpage/', formpageview, name='formpage'),
path('registration/', register, name = 'registration'),
path('login/',user_login, name='user_login'), 
#path('user_logout/' ,user_logout, name='user_logout'),  
]