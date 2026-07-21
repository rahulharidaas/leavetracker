# Leave Tracker

A multi-tenant Leave Management SaaS application built with Django.

## Features

- **Super Admin** — manages all companies, sends invites to company admins
- **Company Admin** — manages employees, departments, and leave requests
- **Employee** — applies for leaves, views leave history and balance
- **Invite-based signup** — users join via email invite links (expires in 24 hours)
- **Role-based login** — each role redirects to their own dashboard

## Tech Stack

- Python 3
- Django
- SQLite (development)
- HTML, CSS, JavaScript

## System Hierarchy

```
Super Admin
    └── Company Admin (Company A)
            └── Department
                    └── Employees
    └── Company Admin (Company B)
            └── Department
                    └── Employees
```

## Database Models

| Model | Description |
|---|---|
| `auth_user` | Django built-in user model |
| `Company` | Stores company details |
| `Department` | Belongs to a company |
| `UserProfile` | Links user to company, department and role |
| `InviteToken` | UUID-based invite tokens sent via email |

## Setup & Installation

1. **Clone the repository**
```
git clone https://github.com/rahulharidaas/leavetracker.git
cd leavetracker
```

2. **Install dependencies**
```
pip install django python-decouple
```

3. **Create a `.env` file** in the root directory
```
SECRET_KEY=your-django-secret-key
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

4. **Run migrations**
```
python manage.py migrate
```

5. **Create a Super Admin user**
```
python manage.py createsuperuser
```

Then manually set the role in the database or shell:
```python
python manage.py shell
from django.contrib.auth.models import User
from accounts.models import UserProfile
user = User.objects.get(username='your-username')
UserProfile.objects.create(user=user, role='superadmin')
```

6. **Run the server**
```
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/accounts/login/`

## Email Configuration

This project uses Gmail SMTP for sending invite emails. Make sure to:
- Enable 2-Factor Authentication on your Gmail account
- Generate an **App Password** and add it to `.env`

## Project Status

🚧 Under active development

- [x] Super Admin Dashboard
- [x] Company invite flow
- [x] Admin Dashboard
- [x] Employee invite flow
- [x] Role-based login & redirect
- [ ] Departments management
- [ ] Leave types & balance
- [ ] Leave requests & approvals
- [ ] Employee Dashboard


## Steps To Follow

Phase 1 — Setup

Install Python & VS Code
Install Django — pip install django
Create project — django-admin startproject leavetracker
Create app — python manage.py startapp accounts
Phase 2 — Models
5. Create models — Company, Department, UserProfile, InviteToken
6. Run migrations

Phase 3 — Auth
7. Login / Logout views
8. Role-based redirect

Phase 4 — Super Admin
9. Super Admin dashboard
10. Companies page + invite flow

Phase 5 — Admin
11. Admin dashboard
12. Employees page + invite flow

Phase 6 — Signup
13. Two-step admin signup
14. Employee signup
