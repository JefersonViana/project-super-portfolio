from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    github = models.URLField(blank=False, max_length=500)
    linkedin = models.URLField(blank=False, max_length=500)
    bio = models.TextField(blank=False, max_length=500)

    def __str__(self):
        return self.name
