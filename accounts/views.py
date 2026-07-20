from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from .models import Company,UserProfile,InviteToken,Department
from django.http import HttpResponse
import uuid
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail


# Create your views here.



def login_view(request):
    message=""

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            profile=UserProfile.objects.get(user=user)
            if profile.role =='superadmin':
                return redirect('superadmin_dashboard')
            elif profile.role == 'admin':
               return redirect('admin_dashboard')
            elif profile.role ==  'employee':
                 return HttpResponse("Welcome Employee!")
        else:
            message= "Invalid username or password"
    return render(request,'accounts/login.html', {'message':message})

def logout_view(request):
    logout(request)
    return redirect('login')



def superadmin_dashboard(request):
    

    total_companies=Company.objects.count()
    active_companies=Company.objects.filter(is_active=True).count()
    inactive_companies=Company.objects.filter(is_active=False).count()


    return render(request, 'superadmin_dashboard.html', {
        'total_companies': total_companies,
        'active_companies': active_companies,
        'inactive_companies' : inactive_companies,
        
    })

def superadmin_companies(request):
    message = ""
    
    if request.method == "POST":
        email = request.POST.get('email')
        role = request.POST.get('role')
        token = uuid.uuid4()
        expires_at = timezone.now() + timedelta(hours=24)
        InviteToken.objects.create(
            email=email,
            token=token,
            role=role,
            expires_at=expires_at,
        )
        invite_link = f"http://127.0.0.1:8000/accounts/signup/{token}/"
        send_mail(
            'You are invited to Join Leave Tracker',
            f'Click the link to sign up: {invite_link}',
            'rahulharidaas@gmail.com',
            [email],
        )
        message = "Invite sent successfully!"
    
    companies = Company.objects.all()   # ← outside the if block
    
    return render(request, 'superadmin_companies.html', {
        'message': message,
        'companies': companies,
    })


def superadmin_settings(request):
    return render(request,'superadmin_settings.html')


def signup_view(request, token):
    message = ""
    
    try:
        invite = InviteToken.objects.get(token=token)
    except InviteToken.DoesNotExist:
        return HttpResponse("Invalid invite link.")
    
    if invite.is_used:
        return HttpResponse("This invite link has already been used.")
    
    if invite.expires_at < timezone.now():
        return HttpResponse("This invite link has expired.")
    
    if invite.role =='admin':
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            company_name = request.POST.get('company_name')
            company_email = request.POST.get('company_email')
            company_address = request.POST.get('company_address')

            if User.objects.filter(username=username).exists():
                message = "Username already taken!"
            else:
                company = Company.objects.create(
                    name=company_name,
                    email=company_email,
                    address=company_address,
                )
                user = User.objects.create_user(
                    username=username,
                    email=invite.email,
                    password=password
                )
                UserProfile.objects.create(
                    user=user,
                    role=invite.role,
                    company=company,
                )
                invite.is_used = True
                invite.save()
                return render(request, 'accounts/signup.html', {
                    'message': "Account created successfully! Redirecting to login...",
                    'invite': invite,
                    'success': True,
                })

            return render(request, 'accounts/signup.html', {
                'message': message,
                'invite': invite,
            })
    elif invite.role == 'employee':
        if request.method == "POST":
            password = request.POST.get('password')
            user = User.objects.create_user(
                username=invite.email,
                email=invite.email,
                password=password
            )
            UserProfile.objects.create(
                user=user,
                role='employee',
                company=invite.company,
                employee_id=invite.employee_id,
                job_title=invite.job_title,
            )
            invite.is_used = True
            invite.save()
            return render(request, 'accounts/signup.html', {
                'message': "Account created successfully! Redirecting to login...",
                'invite': invite,
                'success': True,
            })

    return render(request, 'accounts/signup.html', {
        'message': message,
        'invite': invite,
    })

        


def admin_dashboard(request):
    profile=UserProfile.objects.get(user=request.user)
    company=profile.company

    total_employees=UserProfile.objects.filter(company=company, role='employee').count()
    total_departments=Department.objects.filter(company=company).count()

    return render(request, 'admin_dashboard.html', {
        'company': company,
        'total_employees': total_employees,
        'total_departments': total_departments,
    })


def admin_employees(request):
    profile=UserProfile.objects.get(user=request.user)
    company=profile.company
    message=""

    if request.method=="POST":
        email=request.POST.get('email')
        employee_id=request.POST.get('employee_id')
        job_title=request.POST.get('job_title')
        token=uuid.uuid4()
        expires_at=timezone.now() + timedelta(hours=24)
        InviteToken.objects.create(
            email=email,
            token=token,
            role='employee',
            company=company,
            expires_at=expires_at,
            employee_id=employee_id,
            job_title=job_title,
        )
        invite_link=f"http://127.0.0.1:8000/accounts/signup/{token}/"
        send_mail(
            'You are invited to Join Leave Tracker',
            f'Click the link to sign up: {invite_link}',
            'rahulharidaas@gmail.com',
            [email],
        )
        message = "Invite sent successfully!"
    employees=UserProfile.objects.filter(company=company,role='employee')

    return render(request, 'admin_employees.html',{
        'company': company,
        'employees': employees,
        'message':message,
    })