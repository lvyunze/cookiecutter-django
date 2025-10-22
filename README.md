# Cookiecutter Django Template

[中文](README_zh.md) | English

## Overview

This is a Cookiecutter template for quickly bootstrapping Django projects with best practices and modern development workflows.

## Features

- 🚀 **Quick Start**: Generate a complete Django project structure in seconds
- 🎨 **Modern Stack**: Pre-configured with Django best practices
- 👥 **User Management**: Built-in custom user model and authentication
- 🔒 **Security**: Security settings configured out of the box
- 📦 **Static Files**: Organized static files structure (CSS, JS)
- 🎯 **Admin Interface**: Customized Django admin templates
- 🔐 **Two-Factor Authentication**: Optional 2FA support templates
- ⚙️ **Environment Variables**: `.env` file support for configuration management

## Project Structure

```
{{cookiecutter.project_name}}/
├── static/                 # Static files (CSS, JS)
│   ├── css/
│   └── js/
├── templates/              # HTML templates
│   ├── admin/             # Custom admin templates
│   ├── two_factor/        # 2FA templates
│   └── base.html          # Base template
├── users/                  # User app
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── {{cookiecutter.project_name|upper}}/  # Main project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── .env.example
```

## Prerequisites

- Python 3.8+
- pip
- cookiecutter

## Installation

### 1. Install Cookiecutter

```bash
pip install cookiecutter
```

### 2. Generate Project

```bash
cookiecutter https://github.com/yourusername/cookiecutter-django
```

Or if you have cloned this repository locally:

```bash
cookiecutter /path/to/cookiecutter-django
```

### 3. Follow the Prompts

You will be prompted to enter:
- **project_name**: Your project name (e.g., "My Awesome Project")

The template will automatically generate a project with the appropriate structure.

## Post-Generation Setup

After generating your project:

### 1. Navigate to Project Directory

```bash
cd <your_project_name>
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
# Edit .env file with your configuration
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see your application.

## Customization

### Template Variables

The template uses custom Jinja2 delimiters to avoid conflicts with Django templates:

- Variable: `<< variable >>`
- Block: `<<% block %>>` 
- Comment: `<<# comment #>>`

### Files Not Rendered

The following file types are copied without Jinja2 rendering:
- JavaScript files (*.js)
- CSS files (*.css)
- Minified files (*.min.js, *.min.css)
- Image files (*.jpg, *.jpeg, *.png, *.gif, *.svg, *.ico)
- Font files (*.woff, *.woff2, *.ttf, *.eot)

## Included Apps

### Users App

A custom user application with:
- Custom user model extending Django's AbstractUser
- User admin configuration
- Ready for customization

## Development

### Pre-Generation Hook

The `hooks/pre_gen_project.py` script runs before project generation to validate inputs and perform any necessary setup.

## Best Practices

This template follows Django best practices:

- ✅ Custom user model from the start
- ✅ Environment-based configuration
- ✅ Organized static files and templates
- ✅ Proper app structure
- ✅ Security settings configured
- ✅ Ready for deployment

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Happy Coding!** 🎉
