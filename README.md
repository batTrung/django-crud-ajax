# Hướng dẫn thực hiện CRUD bằng Ajax/Jquery

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.1-brightgreen.svg)](https://djangoproject.com)

<a target="_blank" href="https://www.djangobat.com/blog/huong-dan-thuc-hien-crud-voi-ajax/"><img src="https://www.djangobat.com/media/posts/2019/10/03/djang-crud.jpg" alt="" /></a>

## BLOG 

[https://www.djangobat.com/](https://www.djangobat.com/)

## Cài đặt

Đầu tiên, tải repository về máy tính:

```bash
git clone https://github.com/batTrung/django-crud-ajax.git
```

Cài đặt requirements:

```bash
cd django-crud-ajax
pip install -r requirements.txt
```

Áp dụng migrations:

```bash
python manage.py makemigrations users
python manage.py migrate
```

Chạy development server

```bash
python manage.py runserver
```

Mở Chrome hay FireFox : **127.0.0.1:8000**