from django.urls import path
from . import views

urlpatterns = [
    path('', views.IncomplatedTaskView.as_view(), name='incompleted_tasks'),
    path('all_task/', views.TaskListViews.as_view(), name='show_tasks'),
    path('input_task/', views.TaskInputViews.as_view(), name='input_task'),
    path('delete_task/<int:pk>/', views.TaskDeleteView.as_view(), name='delete_task'),
    path('edit_task/<int:pk>', views.TaskUpdateView.as_view(), name='update'),
    path('complate_task/<int:pk>/', views.CompleteTaskView.as_view(), name='complete_task'),
    path('completed_task/', views.CompleteTasksListView.as_view(), name='completed_tasks'),
]
