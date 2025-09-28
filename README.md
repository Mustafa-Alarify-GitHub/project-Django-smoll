# Django Project Setup Guide

This guide explains the complete steps to create and run a Django project from scratch.

## Prerequisites

- Python 3.6 or later
- pip (Python package manager)

## Setup Steps

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

#### On Windows:
```bash
venv\Scripts\activate
```

#### On Linux/Mac:
```bash
source venv/bin/activate
```

### 3. Install Django

```bash
pip install django
```

### 4. Create Django Project

```bash
django-admin startproject myproject
```

### 5. Navigate to Project Directory

```bash
cd myproject
```

### 6. Run Initial Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```
Follow the prompts to enter:
- Username
- Email address (optional)
- Password

### 8. Collect Static Files

```bash
python manage.py collectstatic
```

### 9. Run Development Server

```bash
python manage.py runserver
```

### 10. Access Your Project

- Main site: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv/
└── db.sqlite3
```

## Common Commands

| Command | Description |
|---------|-------------|
| `python manage.py runserver` | Start development server |
| `python manage.py makemigrations` | Create migration files |
| `python manage.py migrate` | Apply database migrations |
| `python manage.py createsuperuser` | Create admin user |
| `python manage.py collectstatic` | Collect static files |
| `python manage.py startapp appname` | Create new Django app |

## Deactivation

To deactivate the virtual environment when finished:

```bash
deactivate
```

## Notes

- The virtual environment (`venv/`) should be added to `.gitignore` if using Git
- Database file `db.sqlite3` will be created after running migrations
- Always activate the virtual environment before working on the project
- Use `pip freeze > requirements.txt` to save project dependencies

## Troubleshooting

- If commands don't work, ensure virtual environment is activated
- Check Python version with `python --version`
- Ensure you're in the correct project directory containing `manage.py`