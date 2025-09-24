from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)
def image_upload(instance, name):
    image_name, extension = name.split(".",1)
    return f"jobs/{image_name}.{extension}"
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    description = models.TextField()
    experience = models.IntegerField(default=1)
    published_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
class Apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    job = models.ForeignKey(Job,related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=100)
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name