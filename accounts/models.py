from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="profile/", blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    reset_password_token = models.CharField(max_length=50, blank=True, null=True, default="")
    reset_password_expires = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


# Signal واحد بس
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
