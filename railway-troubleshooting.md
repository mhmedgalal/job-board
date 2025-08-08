# 🔧 حل المشاكل الشائعة في Railway

## مشاكل البناء

### ❌ خطأ في requirements.txt
```
ERROR: Could not find a version that satisfies the requirement
```
**الحل:**
- تحقق من إصدارات الحزم في `requirements.txt`
- تأكد من توافق الإصدارات مع Python 3.11

### ❌ خطأ في Python version
```
ERROR: Python version not supported
```
**الحل:**
- تأكد من وجود `runtime.txt` مع `python-3.11.7`
- تحقق من إعدادات `nixpacks.toml`

### ❌ خطأ في static files
```
ERROR: collectstatic failed
```
**الحل:**
- تأكد من وجود مجلد `static/`
- تحقق من إعدادات `STATICFILES_DIRS` في `settings.py`

## مشاكل قاعدة البيانات

### ❌ خطأ في الاتصال بقاعدة البيانات
```
ERROR: connection to database failed
```
**الحل:**
- تأكد من إضافة خدمة PostgreSQL
- تحقق من متغير `DATABASE_URL`
- تأكد من تشغيل الهجرات

### ❌ خطأ في الهجرات
```
ERROR: migrations failed
```
**الحل:**
- تحقق من وجود جميع ملفات الهجرات
- تأكد من عدم وجود تضارب في الهجرات
- جرب `python manage.py makemigrations` محلياً

## مشاكل التطبيق

### ❌ الموقع لا يفتح
```
ERROR: Application failed to start
```
**الحل:**
- تحقق من سجلات التطبيق في Railway
- تأكد من صحة `Procfile`
- تحقق من متغير `PORT`

### ❌ خطأ 500 Internal Server Error
```
ERROR: 500 Internal Server Error
```
**الحل:**
- تحقق من `DEBUG=False` في الإنتاج
- تأكد من إعدادات `ALLOWED_HOSTS`
- تحقق من سجلات Django

### ❌ خطأ في static files
```
ERROR: Static files not found
```
**الحل:**
- تأكد من تشغيل `collectstatic`
- تحقق من إعدادات `STATIC_ROOT`
- تأكد من إعدادات `whitenoise`

## مشاكل الأمان

### ❌ خطأ CSRF
```
ERROR: CSRF verification failed
```
**الحل:**
- تأكد من إعدادات `CSRF_COOKIE_SECURE`
- تحقق من `SECURE_SSL_REDIRECT`

### ❌ خطأ في HTTPS
```
ERROR: Mixed content
```
**الحل:**
- تأكد من `SECURE_SSL_REDIRECT=True`
- تحقق من إعدادات `SECURE_PROXY_SSL_HEADER`

## مشاكل البريد الإلكتروني

### ❌ خطأ في إرسال البريد
```
ERROR: Email sending failed
```
**الحل:**
- تأكد من متغيرات `EMAIL_USER` و `EMAIL_PASSWORD`
- استخدم كلمة مرور تطبيق Gmail
- تحقق من إعدادات SMTP

## مشاكل المستخدم المشرف

### ❌ لا يمكن إنشاء مستخدم مشرف
```
ERROR: Superuser creation failed
```
**الحل:**
- تأكد من متغيرات `DJANGO_SUPERUSER_*`
- تحقق من أن قاعدة البيانات متصلة
- جرب إنشاء المستخدم يدوياً

## مشاكل الأداء

### ❌ الموقع بطيء
```
ERROR: Slow response times
```
**الحل:**
- تحقق من إعدادات `gunicorn`
- أضف `--workers` أكثر
- تحقق من قاعدة البيانات

### ❌ استهلاك ذاكرة عالي
```
ERROR: High memory usage
```
**الحل:**
- قلل عدد `workers` في gunicorn
- تحقق من تسريب الذاكرة
- استخدم `--max-requests`

## خطوات التشخيص

### 1. تحقق من السجلات
```bash
# في Railway Dashboard
# اذهب إلى "Deployments" → "View Logs"
```

### 2. تحقق من المتغيرات البيئية
```bash
# في Railway Dashboard
# اذهب إلى "Variables"
```

### 3. اختبر محلياً
```bash
# اختبر نفس الإعدادات محلياً
python manage.py runserver
```

### 4. تحقق من قاعدة البيانات
```bash
# في Railway Dashboard
# اذهب إلى "Database" → "Connect"
```

## نصائح عامة

### ✅ أفضل الممارسات
- استخدم متغيرات بيئية للبيانات الحساسة
- تأكد من `DEBUG=False` في الإنتاج
- اختبر محلياً قبل النشر
- راقب السجلات بانتظام

### ✅ أدوات مفيدة
- Railway CLI للتحكم المحلي
- Django Debug Toolbar للتطوير
- Sentry لمراقبة الأخطاء

### ✅ روابط مفيدة
- [Railway Documentation](https://docs.railway.app/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/)
- [Gunicorn Configuration](https://docs.gunicorn.org/en/stable/configure.html) 