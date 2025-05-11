from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.landing_page, name='landing'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing'), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('documents/', views.document_list, name='documents'),
    path('subscriptions/', views.subscription_list, name='subscriptions'),
    path('reminders/', views.reminder_list, name='reminders'),

    path('documents/add/', views.add_document, name='add_document'),
    path('subscriptions/add/', views.add_subscription, name='add_subscription'),
    path('reminders/add/', views.add_reminder, name='add_reminder'),

    path('documents/edit/<int:pk>/', views.edit_document, name='edit_document'),
    path('documents/delete/<int:pk>/', views.delete_document, name='delete_document'),

    path('subscriptions/edit/<int:pk>/', views.edit_subscription, name='edit_subscription'),
    path('subscriptions/delete/<int:pk>/', views.delete_subscription, name='delete_subscription'),

    path('reminders/edit/<int:pk>/', views.edit_reminder, name='edit_reminder'),
    path('reminders/delete/<int:pk>/', views.delete_reminder, name='delete_reminder'),

]

