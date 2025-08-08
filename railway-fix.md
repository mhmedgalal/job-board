# 🔧 حل مشكلة "pip: command not found"

## المشكلة
```
/bin/bash: line 1: pip: command not found
"pip install -r requirements.txt" did not complete successfully: exit code: 127
```

## الحلول

### ✅ الحل الأول: تحديث nixpacks.toml
تم تحديث `nixpacks.toml` لإضافة `pip` إلى `nixPkgs`:

```toml
[phases.setup]
nixPkgs = ["python311", "postgresql", "pip"]
```

### ✅ الحل الثاني: استخدام python -m pip
إذا استمرت المشكلة، يمكن تغيير الأمر في `nixpacks.toml`:

```toml
[phases.install]
cmds = ["python -m pip install -r requirements.txt"]
```

### ✅ الحل الثالث: استخدام requirements.txt مبسط
تأكد من أن `requirements.txt` لا يحتوي على تكرار:

```
asgiref==3.8.1
dj-database-url==2.1.0
Django==5.1.7
django-bootstrap5==23.3
django-filter==23.5
gunicorn==21.2.0
packaging==25.0
Pillow==10.1.0
psycopg2-binary==2.9.9
python-dotenv==1.0.0
sqlparse==0.5.3
typing_extensions==4.14.1
tzdata==2025.1
whitenoise==6.6.0
```

## خطوات التطبيق

### 1. ارفع التحديثات
```bash
git add .
git commit -m "Fix pip command not found issue"
git push origin main
```

### 2. أعد النشر في Railway
- اذهب إلى Railway Dashboard
- اضغط "Redeploy" أو انتظر النشر التلقائي

### 3. راقب السجلات
- اذهب إلى "Deployments"
- تحقق من سجلات البناء الجديدة

## بدائل إضافية

### استخدام Dockerfile
إذا استمرت المشكلة، يمكن إنشاء `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "project.wsgi", "--bind", "0.0.0.0:8000"]
```

### استخدام buildpacks
يمكن أيضاً استخدام Heroku buildpacks في Railway.

## ملاحظات مهمة

- ✅ تم إضافة `pip` إلى `nixPkgs`
- ✅ تم تحديث `Procfile` مع إعدادات أفضل
- ✅ تم تنظيف `requirements.txt`
- ✅ تم تحديث `railway.toml`

## إذا استمرت المشكلة

1. تحقق من سجلات Railway
2. جرب الحلول البديلة
3. راجع `railway-troubleshooting.md`
4. تأكد من أن جميع الملفات محدثة
