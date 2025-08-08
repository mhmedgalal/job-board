# 🚀 النشر السريع على Railway

## الخطوات السريعة (5 دقائق)

### 1. ارفع المشروع لـ GitHub
```bash
git add .
git commit -m "Ready for Railway deployment"
git push origin main
```

### 2. اذهب لـ Railway
- [railway.app](https://railway.app)
- سجل دخول بـ GitHub

### 3. أنشئ مشروع جديد
- "New Project" → "Deploy from GitHub repo"
- اختر المستودع الخاص بك
- "Deploy Now"

### 4. أضف قاعدة البيانات
- "New Service" → "Database" → "PostgreSQL"

### 5. أضف المتغيرات البيئية
في "Variables" أضف:
```
DJANGO_SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=False
```

### 6. انتظر النشر
- اذهب لـ "Deployments" لمراقبة العملية
- اضغط على الرابط المولود

## ✅ تم! موقعك جاهز

### لإنشاء مستخدم مشرف:
أضف هذه المتغيرات مؤقتاً:
```
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=your-password
```

ثم أعد النشر واحذف المتغيرات.

## 🔧 استكشاف الأخطاء

### إذا لم يعمل:
1. تحقق من سجلات "Deployments"
2. تأكد من المتغيرات البيئية
3. تأكد من وجود قاعدة البيانات

### للمساعدة:
- راجع `railway-deploy.md` للتعليمات المفصلة
- تحقق من `railway-setup.md` للمتغيرات البيئية 