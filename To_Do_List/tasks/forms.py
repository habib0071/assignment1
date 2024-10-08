from django import forms
from tasks.models import TaskModel

class TaskModelFrom(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']
