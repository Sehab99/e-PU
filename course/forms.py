from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class AddCourse(ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'


class AddTopic(ModelForm):
    class Meta:
        model = Topics
        fields = '__all__'
