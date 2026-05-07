# 🛒 DiplomaShop — Full-Stack Django E-Commerce Platform

Live Demo: https://diploma-shop-my81.onrender.com

---

## 📌 Project Overview

DiplomaShop is a production-style e-commerce web application built with Django and PostgreSQL.

The project demonstrates real-world backend and full-stack development skills, including:

- User authentication
- Shopping cart functionality
- Order processing
- Multilanguage support
- Cloud media storage
- Docker containerization
- Google Analytics integration
- Production deployment

The application follows modern web development practices and simulates a real online store environment.

---

## ✨ Key Features

### 🛍️ E-Commerce Functionality
- Product catalog with categories
- Product detail pages
- Shopping cart system
- Quantity management
- Checkout & order processing
- Order history for authenticated users

### 👤 User Authentication
- User registration
- Login / logout system
- User profile management
- Session-based authentication

### 🌍 Multilingual Support
- English / Ukrainian / Russian languages
- Product and category translations
- django-modeltranslation integration

### ⚙️ Admin Panel
- Product management
- Category management
- Order administration
- Contact & social links management

### 📊 Analytics & Dashboard
- Google Analytics GA4 integration
- Website traffic tracking
- User activity monitoring
- Custom admin analytics dashboard
- Orders statistics
- Products statistics
- Users statistics
- Recent orders monitoring
- Multilanguage dashboard support

### ☁️ Cloud & Deployment
- Cloudinary media storage
- PostgreSQL database
- Production deployment on Render
- Environment variable configuration
- Static file handling with WhiteNoise

### 🐳 Docker Support
- Dockerized Django application
- Docker Compose configuration
- PostgreSQL container
- Local containerized development environment

---

## 🧠 Technology Stack

### Backend
- Python 3.14
- Django 6
- PostgreSQL
- SQLite (local development)

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Django Templates

### DevOps & Deployment
- Docker
- Docker Compose
- Render
- Gunicorn
- WhiteNoise
- Cloudinary

### Tools
- Git
- GitHub
- VS Code / PyCharm

---

## 📂 Main Functional Modules

| Module | Description |
|---|---|
| Shop | Product catalog and product pages |
| Cart | Session-based shopping cart |
| Orders | Checkout and order management |
| Accounts | Authentication and user profiles |
| Contacts | Contact information and social links |
| Languages | Multilanguage support |
| Dashboard | Admin analytics and statistics dashboard |

---

## 🚀 Deployment

The project is deployed on Render with PostgreSQL and Cloudinary integration.

### Production configuration includes:
- PostgreSQL database
- Gunicorn WSGI server
- WhiteNoise static file serving
- Cloudinary media storage
- `.env` environment variables
- Production security settings
- Google Analytics GA4 integration
- Docker local development support

---

## 🔐 Environment Variables

```env
SECRET_KEY=
DEBUG=
DATABASE_URL=
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

---

## 📈 Analytics Features

The project includes integrated Google Analytics GA4 support for tracking:

- Website visitors
- User activity
- Page views
- Traffic analytics

Additionally, a custom Django admin dashboard was implemented for:

- Orders monitoring
- Product statistics
- User statistics
- Recent activity overview

---

## 🐳 Local Development with Docker

The project supports both:

- Standard local Django development (SQLite)
- Dockerized development environment with PostgreSQL

This allows flexible development workflows for local testing and production-style containerized environments.