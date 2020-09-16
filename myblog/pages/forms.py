from django import forms
from django.core import validators
from .models import Author, UserProfileInfo
from django.contrib.auth.models import User




class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField( label="input your email again ")
    text = forms.CharField(widget=forms.Textarea) 
 


    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('emails should match')
        else:
            pass

class NewUserForm(forms.ModelForm):
    class Meta():
        model = Author
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

