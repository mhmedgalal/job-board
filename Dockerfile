FROM python:3.11-slim

# إعداد متغيرات البيئة
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# تحديد مجلد العمل
WORKDIR /app

# تثبيت الحزم النظامية
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# تثبيت الحزم البايثون
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ المشروع
COPY . .

# تجميع الملفات الثابتة
RUN python manage.py collectstatic --noinput

# إظهار المنفذ (للتوثيق فقط)
EXPOSE 8000

# تشغيل gunicorn مع قراءة المنفذ من متغير البيئة PORT
CMD ["sh", "-c", "gunicorn project.wsgi --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120"]
