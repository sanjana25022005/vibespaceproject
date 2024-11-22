from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User



from django import forms
from .models import Goal, Task

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ["title", "description", "start_date", "end_date"]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "priority", "completed"]




class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
