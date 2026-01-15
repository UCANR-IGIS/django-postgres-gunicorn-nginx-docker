# Django Docker Setup with PostgreSQL and Nginx

A production-ready Django application setup with Docker, PostgreSQL, Nginx, and persistent storage for static and media files.

## Features

- Django 5.0.1
- PostgreSQL 14
- Nginx reverse proxy
- Gunicorn WSGI server
- Persistent volumes for database, static, and media files
- Separate development and production configurations

## Project Structure

```
django-docker-setup/
├── django_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
├── .gitignore
├── Dockerfile
├── Dockerfile.prod
├── docker-compose.yml
├── docker-compose.prod.yml
├── manage.py
├── requirements.txt
└── README.md
```

## Development Setup

### Prerequisites

- Docker
- Docker Compose

### Running Development Environment

1. Clone or extract this repository

2. Build and run the containers:
```bash
docker-compose up --build
```

3. Run migrations:
```bash
docker-compose exec web python manage.py migrate
```

4. Create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

5. Access the application:
- Django: http://localhost:8000
- Admin: http://localhost:8000/admin

### Development Commands

```bash
# View logs
docker-compose logs -f

# Stop containers
docker-compose down

# Stop and remove volumes (removes database data)
docker-compose down -v

# Run Django management commands
docker-compose exec web python manage.py <command>

# Access Django shell
docker-compose exec web python manage.py shell

# Run tests
docker-compose exec web python manage.py test
```

## Production Setup

### Prerequisites

- Docker
- Docker Compose

### Running Production Environment

1. Update environment variables in `docker-compose.prod.yml`:
   - `SECRET_KEY`: Generate a secure secret key
   - `ALLOWED_HOSTS`: Add your domain name
   - Database credentials (recommended to use environment files)

2. Build and run production containers:
```bash
docker-compose -f docker-compose.prod.yml up --build -d
```

3. Run migrations:
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
```

4. Create a superuser:
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

5. Access the application:
- Application: http://localhost (port 80)
- Admin: http://localhost/admin

### Production Commands

```bash
# View logs
docker-compose -f docker-compose.prod.yml logs -f

# Stop containers
docker-compose -f docker-compose.prod.yml down

# Restart specific service
docker-compose -f docker-compose.prod.yml restart web

# Collect static files (if needed)
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
```

## Persistent Storage

This setup includes three persistent volumes:

1. **postgres_data**: PostgreSQL database files
2. **static_volume**: Django static files (CSS, JS, images)
3. **media_volume**: User-uploaded media files

These volumes persist data even when containers are stopped or removed.

## File Upload Configuration

The setup is configured to handle file uploads:

- **Static files**: Served at `/static/` URL
- **Media files**: Served at `/media/` URL
- **Max upload size**: 100MB (configurable in nginx.conf)

### Using Media Files in Your Django App

```python
# models.py
from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='documents/')
```

## Nginx Configuration

The nginx service:
- Acts as a reverse proxy to Gunicorn
- Serves static files directly
- Serves media files directly
- Handles client requests up to 100MB

To modify nginx settings, edit `nginx/nginx.conf` and rebuild:
```bash
docker-compose -f docker-compose.prod.yml up --build -d nginx
```

## Environment Variables

### Development (.env or docker-compose.yml)
```
DEBUG=1
SECRET_KEY=your-dev-secret-key
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### Production (.env.prod or docker-compose.prod.yml)
```
DEBUG=0
SECRET_KEY=your-production-secret-key
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=strong-password-here
POSTGRES_HOST=db
POSTGRES_PORT=5432
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## Security Considerations for Production

1. **Change SECRET_KEY**: Generate a unique secret key
2. **Update ALLOWED_HOSTS**: Add your domain
3. **Use strong database passwords**
4. **Use environment files** instead of hardcoding credentials
5. **Enable HTTPS**: Configure SSL/TLS in nginx
6. **Set DEBUG=0**: Never run production with DEBUG=1
7. **Regular backups**: Backup postgres_data volume regularly

## Troubleshooting

### Database Connection Issues
```bash
# Check if database is running
docker-compose ps

# View database logs
docker-compose logs db
```

### Static Files Not Loading
```bash
# Collect static files
docker-compose exec web python manage.py collectstatic --noinput

# Check nginx logs
docker-compose logs nginx
```

### Permission Issues
```bash
# Fix volume permissions
docker-compose exec web chown -R www-data:www-data /code/staticfiles
docker-compose exec web chown -R www-data:www-data /code/mediafiles
```

## Adding Your Django Apps

1. Create your app:
```bash
docker-compose exec web python manage.py startapp myapp
```

2. Add to INSTALLED_APPS in `django_project/settings.py`

3. Create models, views, and URLs as needed

4. Run migrations:
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

## License

This project structure is provided as-is for educational and development purposes.
