from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('submit/', views.submit_request, name='submit_request'),
    path('success/', views.success_request, name='success_request'),
    path('janet/', views.view_requests_janet, name='janet_view'),
    path('reject/<int:pk>/', views.reject_request, name='reject_request'),
    path('forward/<int:pk>/', views.forward_request, name='forward_request'),
    path('finance/', views.view_requests_finance, name='view_requests_finance'),
    path('forward_to_am/<int:pk>/', views.forward_to_admin, name='forward_to_admin'),
    path('administration/', views.view_requests_admin, name='administration_view'),
    path('reject_admin/<int:pk>/', views.reject_request_admin, name='reject_request_admin'),
    path('request/schedule_meeting/<int:pk>/', views.schedule_meeting, name='schedule_meeting'),
    path('scheduled_meetings/', views.view_scheduled_meetings, name='scheduled_meetings'),
    path('SM_dashboard/', views.sm_dashboard, name='sm_dashboard'), 
    path('assign/', views.assign_task, name='assign_task'),
    path('tasks/', views.view_tasks, name='view_tasks'),  
    path('tasks/edit/comments/<int:pk>/', views.edit_task_comments, name='edit_task_comments'),  
    path('tasks/edit/budget/<int:pk>/', views.edit_task_budget, name='edit_task_budget'),  
    path('send/<int:pk>/', views.send_task_to_production, name='send_task_to_production'),  
    path('staff_recruitment/', views.staff_recruitment, name='staff_recruitment'),
    path('send_recruitment/<int:pk>/', views.send_recruitment_to_hr, name='send_recruitment_to_hr'),
    path('budget_increase_request/', views.budget_increase_request, name='budget_increase_request'),
    path('hr_manager/', views.view_hr_manager, name='hr_manager'),
    path('production_manager/', views.production_manager_dashboard, name='production_manager_dashboard'),   
    path('send_recruitment_to_production_from_hr/<int:pk>/', views.send_recruitment_to_production_from_hr, name='send_recruitment_to_production_from_hr'),
    path('reject_recruitment_hr/<int:pk>/', views.reject_recruitment_hr, name='reject_recruitment_hr'),  
    path('budget/send_to_production/<int:pk>/', views.send_budget_request_to_production, name='send_budget_request_to_production'),
    path('budget/reject/<int:pk>/', views.reject_budget_request, name='reject_budget_request'),




]
