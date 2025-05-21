from django.urls import path
from tasks import views

app_name = 'tasks'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task/create/', views.TaskCreation.as_view(), name='task_create'),
    path('update/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),

]