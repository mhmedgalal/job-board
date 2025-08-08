# دليل النشر على Railway - خطوة بخطوة

## 1. إعداد المشروع

### تأكد من وجود الملفات التالية:
- ✅ `requirements.txt` - تبعيات Python
- ✅ `Procfile` - أوامر التشغيل
- ✅ `railway.toml` - إعدادات Railway
- ✅ `nixpacks.toml` - إعدادات البناء
- ✅ `runtime.txt` - إصدار Python
- ✅ `build.sh` - سكريبت البناء
- ✅ `railway-start.sh` - سكريبت التشغيل

## 2. إنشاء حساب Railway

1. اذهب إلى [railway.app](https://railway.app)
2. سجل حساب جديد أو سجل دخول
3. اربط حساب GitHub

## 3. إنشاء مشروع جديد

1. اضغط على "New Project"
2. اختر "Deploy from GitHub repo"
3. اختر المستودع الخاص بك
4. اضغط "Deploy Now"

## 4. إضافة قاعدة البيانات

1. في Railway Dashboard، اضغط "New Service"
2. اختر "Database" ثم "PostgreSQL"
3. سيتم إنشاء قاعدة البيانات تلقائياً
4. سيتم ربط متغير `DATABASE_URL` تلقائياً

## 5. إعداد المتغيرات البيئية

في Railway Dashboard، اذهب إلى "Variables" وأضف:

### Django Settings
```
DJANGO_SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=False
```

### Email Settings (اختياري)
```
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
```

### Security Settings
```
SECURE_SSL_REDIRECT=True
```

## 6. مراقبة النشر

1. اذهب إلى "Deployments" لمراقبة عملية البناء
2. انتظر حتى تكتمل العملية
3. اضغط على الرابط المولود للوصول للموقع

## 7. إنشاء مستخدم مشرف

بعد النشر، اذهب إلى Railway Dashboard:
1. اذهب إلى "Variables"
2. أضف متغير مؤقت:
```
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=your-password
```
3. اذهب إلى "Deployments" وأعد النشر
4. احذف المتغيرات المؤقتة بعد إنشاء المستخدم

## 8. استكشاف الأخطاء

### إذا فشل النشر:
1. تحقق من سجلات البناء في "Deployments"
2. تأكد من صحة المتغيرات البيئية
3. تحقق من أن جميع الملفات موجودة

### إذا لم يعمل الموقع:
1. تحقق من سجلات التطبيق
2. تأكد من أن قاعدة البيانات متصلة
3. تحقق من إعدادات ALLOWED_HOSTS

## 9. تحديث الموقع

للتحديث، ما عليك سوى:
1. ارفع التغييرات إلى GitHub
2. Railway سيكتشف التغييرات تلقائياً
3. سيتم إعادة النشر تلقائياً

## 10. إعدادات إضافية

### Custom Domain
1. اذهب إلى "Settings" في Railway
2. اضغط "Custom Domains"
3. أضف النطاق الخاص بك

### Environment Variables
يمكنك إضافة متغيرات إضافية حسب الحاجة:
```
SENTRY_DSN=your-sentry-dsn
REDIS_URL=your-redis-url
```

## ملاحظات مهمة

- ✅ المشروع مُعد للنشر على Railway
- ✅ قاعدة البيانات ستُهاجر تلقائياً
- ✅ الملفات الثابتة ستُجمع تلقائياً
- ✅ HTTPS مفعل تلقائياً
- ✅ إعدادات الأمان مُحسنة للإنتاج 