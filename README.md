# Job Board Project

مشروع لوحة الوظائف مبني بـ Django

## النشر على Railway

### الخطوات:

1. **إنشاء حساب على Railway**
   - اذهب إلى [railway.app](https://railway.app)
   - سجل حساب جديد أو سجل دخول

2. **ربط المشروع**
   - اضغط على "New Project"
   - اختر "Deploy from GitHub repo"
   - اربط مستودع GitHub الخاص بك

3. **إعداد المتغيرات البيئية**
   في Railway Dashboard، أضف هذه المتغيرات البيئية:
   ```
   DJANGO_SECRET_KEY=your-secret-key-here
   DEBUG=False
   DATABASE_URL=postgresql://... (سيتم إنشاؤه تلقائياً)
   EMAIL_USER=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   ```

4. **إعداد قاعدة البيانات**
   - في Railway، أضف خدمة PostgreSQL
   - سيتم ربطها تلقائياً مع متغير DATABASE_URL

5. **النشر**
   - Railway سيقوم ببناء وتشغيل المشروع تلقائياً
   - يمكنك مراقبة السجلات في Railway Dashboard

### الملفات المطلوبة للنشر:
- `requirements.txt` - تبعيات Python
- `Procfile` - أوامر التشغيل
- `railway.json` - إعدادات Railway
- `nixpacks.toml` - إعدادات البناء
- `runtime.txt` - إصدار Python

### ملاحظات مهمة:
- تأكد من أن DEBUG=False في الإنتاج
- استخدم متغيرات بيئية للبيانات الحساسة
- قاعدة البيانات ستكون PostgreSQL في الإنتاج
- الملفات الثابتة ستُجمع تلقائياً

## التطوير المحلي

```bash
# تثبيت التبعيات
pip install -r requirements.txt

# تشغيل الهجرات
python manage.py migrate

# إنشاء مستخدم مشرف
python manage.py createsuperuser

# تشغيل الخادم
python manage.py runserver
```

## الميزات:
- نظام تسجيل دخول وتسجيل خروج
- نشر وإدارة الوظائف
- نظام تصفية وبحث
- مدونة
- نظام تواصل
- واجهة مستخدم حديثة مع Bootstrap 5 