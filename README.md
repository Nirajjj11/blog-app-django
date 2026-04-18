# Django News Blog Platform

[![Django](https://img.shields.io/badge/Django-6.0.4-green.svg)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A robust, scalable news/blog platform built with Django, featuring role-based user management, content moderation workflow, and interactive user engagement features. Designed for modern web applications with clean architecture and best practices.

## 🚀 Features

### Core Functionality
- **User Authentication & Authorization**: Custom user model with role-based permissions (Author, Editor, Admin)
- **Content Management**: Full CRUD operations for blog posts with status workflow
- **Content Moderation**: Editorial review system with approval/rejection workflow
- **Interactive Features**: Like/dislike system and threaded comments
- **Responsive Design**: Clean, mobile-friendly templates using Bootstrap

### Technical Highlights
- **Custom User Model**: Extends Django's AbstractUser for flexible role management
- **Status Workflow**: Draft → Pending → Published/Rejected lifecycle
- **Class-Based Views**: Leverages Django's generic views for maintainable code
- **Template Inheritance**: Modular template structure with base.html
- **Database Design**: Normalized schema with proper relationships
- **Security**: CSRF protection, authentication middleware, and secure redirects

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Workflow](#workflow)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## 🛠 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (venv or virtualenv)

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/django-news-blog.git
   cd django-news-blog
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django
   # If you have a requirements.txt file, use:
   # pip install -r requirements.txt
   ```

4. **Navigate to Project Directory**
   ```bash
   cd news_project
   ```

5. **Run Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   Open your browser and navigate to `http://127.0.0.1:8000/`

## 📖 Usage

### User Roles & Permissions

#### Regular Users
- View published blog posts
- Register and login
- Like/dislike posts
- Add comments

#### Authors
- All regular user permissions
- Create new blog posts (saved as drafts)
- Edit their own posts
- Submit posts for editorial review
- Delete their own posts

#### Editors
- All author permissions
- View pending posts in editorial panel
- Approve or reject submitted posts
- Moderate content

#### Administrators
- Full system access via Django Admin
- Manage all users and content
- Assign user roles

### Content Workflow

1. **Creation**: Authors create posts in draft status
2. **Submission**: Authors submit drafts for review (status: pending)
3. **Review**: Editors review pending posts
4. **Publication**: Editors approve posts (status: published) or reject them
5. **Engagement**: Users can like, dislike, and comment on published posts

## 🏗 Project Structure

```
news_project/
├── db.sqlite3                    # SQLite database file
├── manage.py                     # Django management script
├── accounts/                     # User management app
│   ├── __init__.py
│   ├── admin.py                  # Admin interface configuration
│   ├── apps.py                   # App configuration
│   ├── forms.py                  # Custom user forms
│   ├── models.py                 # Custom user model
│   ├── tests.py                  # Unit tests
│   ├── urls.py                   # URL patterns
│   ├── views.py                  # View logic
│   └── migrations/               # Database migrations
│       ├── __init__.py
│       └── 0001_initial.py
├── blog/                         # Blog content app
│   ├── __init__.py
│   ├── admin.py                  # Admin interface
│   ├── apps.py                   # App configuration
│   ├── models.py                 # Blog, Like, Comment models
│   ├── tests.py                  # Unit tests
│   ├── urls.py                   # URL patterns
│   ├── views.py                  # View logic
│   └── migrations/               # Database migrations
│       ├── __init__.py
│       └── 0001_initial.py
├── news_project/                 # Main Django project
│   ├── __init__.py
│   ├── asgi.py                   # ASGI configuration
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Root URL configuration
│   ├── wsgi.py                   # WSGI configuration
│   └── __pycache__/              # Python cache files
└── templates/                    # HTML templates
    ├── base.html                 # Base template
    ├── blog/                     # Blog-specific templates
    │   ├── blog_delete.html
    │   ├── blog_detail.html
    │   ├── blog_form.html
    │   ├── blog_list.html
    │   └── pending_list.html
    └── registration/             # Authentication templates
        ├── login.html
        └── signup.html
```

### Key Architecture Decisions

- **App Separation**: `accounts` for user management, `blog` for content
- **Template Organization**: Centralized templates with inheritance
- **Model Design**: Normalized relationships with proper foreign keys
- **View Patterns**: Mix of class-based and function-based views
- **URL Structure**: RESTful URL patterns with meaningful names

## 🔄 Workflow

### Development Workflow
1. **Feature Branch**: Create feature branches for new functionality
2. **Code Development**: Implement features following Django best practices
3. **Testing**: Write and run unit tests
4. **Migration**: Create database migrations for model changes
5. **Review**: Submit pull requests for code review
6. **Deployment**: Merge to main branch and deploy

### Content Workflow
```
Draft → Submit for Review → Editorial Review → Publish/Reject
   ↓           ↓               ↓              ↓
Author     Author          Editor        Editor
```

## 🛠 Technologies

- **Backend**: Django 6.0.4
- **Database**: SQLite (development), PostgreSQL/MySQL (production)
- **Frontend**: HTML5, CSS3, Bootstrap
- **Authentication**: Django's built-in auth system
- **Template Engine**: Django Templates
- **Version Control**: Git
- **Deployment**: Ready for Heroku, AWS, DigitalOcean

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write comprehensive docstrings
- Add unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django community for excellent documentation
- Open source contributors
- Bootstrap for responsive design components

---

**Built with ❤️ using Django**