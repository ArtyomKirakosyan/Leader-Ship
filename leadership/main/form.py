from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Message
class MessageModelForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

class Create(UserCreationForm):
    class Meta:
        model=User
        fields=('username',"email",'password1','password2')