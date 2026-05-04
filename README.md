# 🛒 DiplomaShop — Django E-commerce Project

Live Demo: https://diploma-shop-my81.onrender.com

---

## 📌 About the Project

DiplomaShop is a full-featured e-commerce web application built with Django.

The project demonstrates real-world backend development skills, including:

- User authentication
- Shopping cart functionality
- Order processing
- Multilanguage support (RU / UK / EN)
- Admin panel for product management
- Cloud image storage
- Production deployment

---

## 🚀 Features

### 🛍️ Shop
- Product catalog with categories
- Product detail pages
- Search across multiple languages
- Multilanguage support (django-modeltranslation)

### 🛒 Cart
- Add/remove products
- Update quantity
- Session-based cart

### 👤 User System
- Registration & login
- Profile editing
- Order history

### 📦 Orders
- Checkout system
- Order storage in database

### 🌍 Multilanguage
- RU / UK / EN support
- Translated fields for products and categories

### 📞 Contacts
- Contact information stored in database
- Social links support

---

## 🧠 Tech Stack

- Python 3.14
- Django 6
- Bootstrap 5
- SQLite (development)
- PostgreSQL (production)
- Cloudinary (media storage)
- WhiteNoise (static files)
- Render (deployment)

---

## ⚙️ Deployment

The project is deployed on Render:

👉 https://diploma-shop-my81.onrender.com

### Production setup includes:

- PostgreSQL database
- Environment variables (.env)
- Gunicorn server
- Static files via WhiteNoise
- Media files via Cloudinary

---

## 🔐 Environment Variables

```env
SECRET_KEY=
DEBUG=
DATABASE_URL=
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=