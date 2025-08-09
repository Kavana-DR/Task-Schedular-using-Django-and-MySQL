from django.urls import path
from .import views  
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/',views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),
    
    #Auth routes
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logged_out/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]