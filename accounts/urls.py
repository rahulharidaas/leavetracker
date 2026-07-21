
from django.urls import path
from .import views

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



]