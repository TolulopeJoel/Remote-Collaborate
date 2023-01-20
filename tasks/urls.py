from django.urls import path

from . import views

# app_name = 'tasks'

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('create/', views.TaskCreate.as_view(), name='task_create'),
    path('delete/<int:id>/', views.TaskDelete.as_view(), name='task_delete'),
    path('update/<int:id>/', views.TaskUpdate.as_view(), name='task_edit'),
    path('<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
]