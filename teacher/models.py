from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='teacher/')
    role = models.CharField(max_length=221)
    bio = models.TextField()
    social_telegram = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.full_name
