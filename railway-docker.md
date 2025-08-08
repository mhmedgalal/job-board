# 🐳 استخدام Docker في Railway

## إذا فشل Nixpacks

إذا استمرت مشكلة `pip: command not found`، يمكن استخدام Docker بدلاً من Nixpacks.

## الخطوات

### 1. تأكد من وجود Dockerfile
تم إنشاء `Dockerfile` في المشروع.

### 2. في Railway Dashboard
1. اذهب إلى مشروعك في Railway
2. اذهب إلى "Settings"
3. في "Build & Deploy" section
4. غيّر "Builder" من "Nixpacks" إلى "Dockerfile"

### 3. أعد النشر
- اضغط "Redeploy" أو انتظر النشر التلقائي

## مزايا استخدام Docker

### ✅ المزايا:
- تحكم كامل في البيئة
- حل مشاكل التوافق
- أداء أفضل
- إعدادات مخصصة

### ✅ ما يتضمنه Dockerfile:
- Python 3.11
- PostgreSQL client
- جميع التبعيات
- جمع الملفات الثابتة
- Gunicorn مُعد

## إعدادات إضافية

### متغيرات بيئية
أضف هذه المتغيرات في Railway:
```
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=postgresql://... (تلقائي)
```

### قاعدة البيانات
- أضف خدمة PostgreSQL
- سيتم ربطها تلقائياً

## مراقبة النشر

### سجلات البناء
- اذهب إلى "Deployments"
- تحقق من سجلات Docker build

### سجلات التطبيق
- اذهب إلى "Logs"
- راقب تشغيل التطبيق

## استكشاف الأخطاء

### إذا فشل بناء Docker:
1. تحقق من `Dockerfile`
2. تأكد من `requirements.txt`
3. تحقق من سجلات البناء

### إذا لم يعمل التطبيق:
1. تحقق من سجلات التطبيق
2. تأكد من المتغيرات البيئية
3. تحقق من قاعدة البيانات

## العودة لـ Nixpacks

إذا أردت العودة لـ Nixpacks:
1. اذهب إلى "Settings"
2. غيّر "Builder" إلى "Nixpacks"
3. أعد النشر

## ملاحظات مهمة

- ✅ Dockerfile جاهز للاستخدام
- ✅ جميع الإعدادات مُعدة
- ✅ يمكن التبديل بين Docker و Nixpacks
- ✅ الأداء سيكون أفضل مع Docker
