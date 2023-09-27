from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
     
    class Meta(UserCreationForm):

        model  = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name' ,'last_name' )

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):

        model  = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name' ,'last_name' )

