from django.shortcuts import render

from tasks.models import TaskModel
from tasks.forms import TaskModelFrom

from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy


# Create your views here.


class TaskInputViews(CreateView):
    model = TaskModel
    template_name = 'input_task.html'
    form_class = TaskModelFrom
    success_url = reverse_lazy('incompleted_tasks')

class TaskListViews(ListView):
    model = TaskModel
    template_name = 'show_tasks.html'
    form_class = TaskModelFrom
    context_object_name = 'task'
    ordering = ['-taskTitle']

class TaskDeleteView(DeleteView):
    model = TaskModel
    template_name = 'delete_task.html'
    success_url = reverse_lazy('show_tasks')


class TaskUpdateView(UpdateView):
    model = TaskModel
    template_name = 'edit_task.html'
    form_class = TaskModelFrom
    success_url = reverse_lazy('show_tasks')

class CompleteTasksListView(ListView):
    model = TaskModel
    template_name  = 'completed_tasks.html'
    context_object_name = 'task'
    
    def get_queryset(self):
        return TaskModel.objects.filter(is_completed = True)
    
class CompleteTaskView(UpdateView):
    model = TaskModel
    fields = []
    template_name = 'confirm_complete.html'
    success_url = reverse_lazy('completed_tasks')

    def form_valid(self, form):
        self.object.is_completed = True 
        self.object.save()
        return super().form_valid(form)
    
class IncomplatedTaskView(ListView):
    model = TaskModel
    template_name  = 'incomplete_tasks.html'
    context_object_name = 'task'
    
    def get_queryset(self):
        return TaskModel.objects.filter(is_completed = False)
