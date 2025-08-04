# 📝 أساسيات إنشاء مشروع Django

---

## 0. إنشاء وتفعيل البيئة الافتراضية (Virtual Environment)

### إنشاء بيئة افتراضية:
```bash
python -m venv venv
```

### تفعيل البيئة الافتراضية:
- **على ويندوز:**
```bash
venv\Scripts\activate
```
- **على لينكس أو ماك:**
```bash
source venv/bin/activate
```

### تثبيت Django داخل البيئة:
```bash
pip install django
```

---

## 1. إنشاء مشروع جديد
```
django-admin startproject project_name
```

---

## 2. إنشاء تطبيق جديد داخل المشروع
```
python manage.py startapp app_name
```

---

## 3. إضافة التطبيق إلى إعدادات المشروع
في ملف `settings.py`:
```python
INSTALLED_APPS = [
    # ... تطبيقات أخرى ...
    'app_name',
]
```

---

## 4. إعداد قاعدة البيانات (افتراضيًا SQLite)
تأكد من إعداد قاعدة البيانات في `settings.py` إذا احتجت.

---

## 5. إنشاء النماذج (Models)
في ملف `models.py`:
```python
from django.db import models

class ModelName(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # ...
```
ثم:
```
python manage.py makemigrations
python manage.py migrate
```

---

## 6. تسجيل النماذج في لوحة الإدارة (Admin)
في ملف `admin.py`:
```python
from .models import ModelName
from django.contrib import admin

admin.site.register(ModelName)
```

إنشاء مستخدم سوبر:
```
python manage.py createsuperuser
```

---

## 7. إنشاء العروض (Views)
في ملف `views.py`:
```python
from django.shortcuts import render

def view_name(request):
    context = {}
    return render(request, 'template.html', context)
```

---

## 8. إعداد الروابط (URLs)
في ملف `urls.py` داخل التطبيق:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('route/', views.view_name, name='view_name'),
]
```
في ملف `urls.py` الرئيسي:
```python
from django.urls import path, include

urlpatterns = [
    path('app/', include('app_name.urls')),
]
```

---

## 9. إنشاء القوالب (Templates)
- أنشئ مجلد `templates` داخل التطبيق أو المشروع.
- أضف ملفات HTML.

---

## 10. تشغيل السيرفر المحلي
```
python manage.py runserver
```
ثم افتح المتصفح على:
```
http://127.0.0.1:8000/
```

---

## ⭐ نصائح سريعة
- استخدم Git لحفظ نسخ من شغلك.
- راجع الأخطاء في التيرمنال أو المتصفح.
- اقرأ رسائل الخطأ جيدًا، غالبًا بتوضح مكان المشكلة.

---

لو عايز شرح لأي جزء بالتفصيل أو إضافة خطوات متقدمة، قولي! 