# تعليمات إعداد Railway

## المتغيرات البيئية المطلوبة

أضف هذه المتغيرات في Railway Dashboard:

### Django Settings
```
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=False
```

### Database
```
DATABASE_URL=postgresql://... (سيتم إنشاؤه تلقائياً عند إضافة PostgreSQL)
```

### Email Settings
```
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
```

### Security Settings
```
SECURE_SSL_REDIRECT=True
```

## خطوات النشر

1. **إنشاء مشروع جديد في Railway**
2. **ربط مستودع GitHub**
3. **إضافة خدمة PostgreSQL**
4. **إضافة المتغيرات البيئية**
5. **انتظار اكتمال البناء والنشر**

## ملاحظات مهمة

- تأكد من أن `DEBUG=False` في الإنتاج
- استخدم كلمة مرور تطبيق Gmail (وليس كلمة المرور العادية)
- قاعدة البيانات ستُهاجر تلقائياً
- الملفات الثابتة ستُجمع تلقائياً 