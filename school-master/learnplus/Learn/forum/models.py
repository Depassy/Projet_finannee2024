# models.py

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify

class Sujet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sujet')
    cours = models.ForeignKey('school.Cours', on_delete=models.CASCADE, related_name='cours_forum', null=True)
    question = models.TextField()
    titre = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Convertir date_add en chaîne pour slugify
        self.slug = '-'.join((slugify(self.titre), slugify(str(self.date_add))))
        super(Sujet, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Sujet'
        verbose_name_plural = 'Sujets'

    def __str__(self):
        return self.titre
