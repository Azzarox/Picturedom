# Picturedom

A photo-sharing social media platform built with **Django** and **PostgreSQL**, similar to Instagram or Pinterest. Users can share, like, comment on, and discover images organized by categories.

**Live Demo:**
- [https://picturedom.onrender.com/](https://picturedom.onrender.com/)
- [https://picturedom.up.railway.app/](https://picturedom.up.railway.app/)

---

## Requirements

- Python 3.9+
- PostgreSQL
- Docker & Docker Compose (optional)

---

## Quick Start

```shell
# Clone the repository
git clone <repository-url>
cd Picturedom

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your database credentials

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Load fixtures (seeds)
python manage.py loaddata fixtures/categories.json
python manage.py loaddata fixtures/users.json
python manage.py loaddata fixtures/superuser.json

# Or create superuser manually
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

**Superuser fixture credentials:**
- Username: `admin`
- Email: `admin@gmail.com`

---

## Tech Stack

- **Django 4.2** - Python web framework
- **PostgreSQL 17** - Database
- **Docker & Docker Compose** - Containerization
- **Cloudinary** - Cloud image storage (production)
- **WhiteNoise** - Static file serving
- **Bootstrap 4** - Frontend styling (via crispy-forms)
- **Pillow** - Image processing
- **Gunicorn** - Production WSGI server

---

## Features

### Photos
- Upload photos (max 8MB) with category organization
- Like/unlike photos
- View photos by category (paginated)
- Browse homepage with most recent photos

### Comments
- Add comments to photos (max 200 characters)
- Like/dislike comments
- Edit and delete your own comments
- Automatic forbidden word filtering

### User Profiles
- User authentication (register, login, logout)
- Edit profile information (name, age, email, profile picture)
- View user statistics (photos, comments, likes received)

### Security & Validation
- Bot protection on all forms
- Email validation (.bg, .com, .edu, .net, .org)
- Profile name validation (letters only)
- Image file size limits (photos: 8MB, profile: 1MB)

---

## Environment Variables

Create a `.env` file in the project root:

```dotenv
# Environment
PROD=false

# Database
DB_URL=

# Other
DEBUG=
SECRET_KEY=
ALLOWED_HOSTS='localhost,127.0.0.1'
CSRF_TRUSTED_ORIGINS='http://localhost,http://something.else.com'

# Cloudinary
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

---

## Docker Setup

The `docker-compose.yml` creates three services:

| Service | Port | Description |
|---------|------|-------------|
| django_app | 8000 | Django development server |
| postgres | 5432 | PostgreSQL database |
| pgadmin | 8080 | Database management GUI |

```shell
# Start all containers
docker compose up

# Stop all containers
docker compose down

# Access Django container shell
docker exec -it <container_id> bash
```

Volumes persist both media files and database data between container restarts.

---

## Project Structure

```
Picturedom/
├── src/                            # Django settings package
│   ├── auth_app/                   # Authentication (register, login)
│   ├── photo/                      # Photo management (CRUD, likes, comments)
│   ├── profile_user/               # User profiles
│   ├── core/                       # Shared utilities & validators
│   ├── settings.py                 # Django configuration
│   └── urls.py                     # URL routing
├── templates/                      # HTML templates
├── static/                         # CSS, JS, images
├── media/                          # User uploads
├── tests/                          # Test suite
├── fixtures/                       # Sample data (seeds)
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── manage.py
├── README.md
└── LICENSE
```

---

## Scripts

```shell
# Run development server
python manage.py runserver

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Load fixtures (seeds)
python manage.py loaddata fixtures/categories.json
python manage.py loaddata fixtures/users.json
python manage.py loaddata fixtures/superuser.json

# Create admin user manually
python manage.py createsuperuser

# Run tests
python manage.py test

# Collect static files (production)
python manage.py collectstatic --noinput
```

---

## Routes

### Public

| Route | Description |
|-------|-------------|
| `/` | Homepage - all photos |
| `/photo/<id>/` | View photo with comments |
| `/photo/categories/<id>/` | Photos by category |
| `/register/` | User registration |
| `/login/` | User login |
| `/logout/` | User logout |
| `/admin/` | Django admin panel |

### Authenticated

| Route | Description |
|-------|-------------|
| `/photo/create/` | Upload new photo |
| `/photo/like/<id>/` | Like/unlike photo |
| `/photo/comments/<id>/` | Add comment |
| `/photo/comments/edit/<id>/` | Edit comment |
| `/photo/comments/delete/<id>/` | Delete comment |
| `/photo/comments/like/<id>/` | Like comment |
| `/photo/comments/dislike/<id>/` | Dislike comment |
| `/user/photos/` | Your uploaded photos |
| `/user/profile/` | Edit your profile |

---

## Testing

```shell
# Run all tests
python manage.py test

# Run specific test module
python manage.py test tests.auth_app.views.test_register_user

# Run with coverage
coverage run manage.py test
coverage report
```

**Note:** Categories are required before users can upload photos. Load them using `python manage.py loaddata fixtures/categories.json` or create them manually via `/admin/`.
