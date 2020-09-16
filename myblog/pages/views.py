from django.shortcuts import render
from .models import Post, Author, Date
from . import forms 
from pages.forms import UserProfileInfoForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse



def homepageview(request):  
    homepage_list = Date.objects.order_by('date')
    list_dict = {'list_records': homepage_list} 
    return render(request, 'pages/home.html', context= list_dict)

def aboutpageview(request):  
    my_dict = {'des':'your welcome'}
    return render(request, 'pages/about.html', context=my_dict)
  
def base(request): 
    return render(request, 'pages/base.html') 
# Create your views here.

def formpageview(request):
    form = forms.NewUserForm

    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True) 
        else:
            print("ERROR FORM COULDNT SAVE")

    return render(request, 'pages/formpage.html', {'form':form})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form  = UserForm(data= request.POST)
        profile_form = UserProfileInfoForm(data= request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
 
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'pages/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

     


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))


            else:
               return HttpResponse('wrong username or password')
        else:
            print('person wan hack in oooh')
            print('him wan use uesrname:{} and password:{}'.format(username, password))
            return HttpResponse("wrong details")
    else:
        return render(request, 'pages/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def special_view(request):
    return HttpResponse("successful good your logged in")