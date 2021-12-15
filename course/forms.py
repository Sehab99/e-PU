from django.forms import ModelForm
from .models import *


class AddCourse(ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'


class AddTopic(ModelForm):
    class Meta:
        model = Topics
        fields = '__all__'
