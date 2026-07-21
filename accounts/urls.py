
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('superadmin/dashboard/', views.superadmin_dashboard, name='superadmin_dashboard'),
    path('superadmin/companies/', views.superadmin_companies, name='superadmin_companies'),
    path('superadmin/settings/', views.superadmin_settings, name='superadmin_settings'),
    path('signup/<uuid:token>/', views.signup_view, name='signup'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/employees/', views.admin_employees, name='admin_employees'),
    path('admin/department/', views.admin_department, name='admin_department'),
    path('admin/settings/', views.admin_settings, name='admin_settings'),
    

    path('password-reset/', auth_views.PasswordResetView.as_view(
        html_email_template_name='registration/password_reset_email.html',
        email_template_name='registration/password_reset_email.txt',
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),




]