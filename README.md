# 📌 Django FAQ API

A multilingual FAQ management system built with **Django**, **Django REST Framework**, and **Redis caching**. Supports **automatic translation** of FAQs using **Google Translate API**.

---

## 📌 Features

✅ **Multilingual Support**: Automatic translation to Hindi & Bengali.  
✅ **WYSIWYG Editor**: CKEditor integration for rich text answers.  
✅ **Fast & Optimized**: Uses **Redis** caching to speed up API responses.  
✅ **REST API**: Fetch FAQs dynamically based on selected language.  
✅ **Unit Tested**: Uses `pytest` and `Django’s unittest` framework.  
✅ **Docker Support**: Easily deployable with Docker & Docker Compose.  

---

## 📌 Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/your-username/django-faq-api.git
cd django-faq-api
```
## Set Up Virtual Environment
```bash
python -m venv env
# Activate the environment:
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
```
## Install Dependencies
```bash
pip install -r requirements.txt
```
## Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
## Create a Superuser
```bash
python manage.py createsuperuser
```
## Start the Server
```bash
python manage.py runserver
```
# Visit http://127.0.0.1:8000/admin to manage FAQs.



