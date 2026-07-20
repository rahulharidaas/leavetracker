
from django.db import models
from django.contrib.auth.models  import User



class Company(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    address=models.TextField()
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Department(models.Model):
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.company.name} - {self.name}"
class UserProfile(models.Model):
    ROLE_CHOICES= [
        ('superadmin' , 'Superadmin'),
        ('admin', 'Admin'),
        ('employee', "Employee"),
    ]

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE, null=True, blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True, blank=True)
    role=models.CharField(max_length=20, choices=ROLE_CHOICES)
    employee_id=models.CharField(max_length=20, blank=True, null=True)
    job_title=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
class InviteToken(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    email=models.EmailField()
    token=models.UUIDField(unique=True)
    role=models.CharField(max_length=20)
    expires_at = models.DateTimeField()
    is_used=models.BooleanField(default=False)
    employee_id=models.CharField(max_length=20, blank=True, null=True)
    job_title=models.CharField(max_length=100, blank=True, null=True)
    



    def __str__(self):
        return f"{self.email} - {self.role}"

