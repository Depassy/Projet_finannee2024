from django.db import models
from school import models as school_models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Salon(models.Model):
    nom = models.CharField(max_length=250, default="Salon sans nom", null=True)
    classe = models.OneToOneField(school_models.Classe, on_delete=models.CASCADE, related_name="class_room", null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    @receiver(post_save, sender=school_models.Classe)
    def create_salon(sender, instance, created, **kwargs):
        if created:
            Salon.objects.create(classe=instance)

    @receiver(post_save, sender=school_models.Classe)
    def save_salon(sender, instance, **kwargs):
        instance.class_room.save()

    class Meta:
        verbose_name = 'Salon'
        verbose_name_plural = 'Salons'

    def __str__(self):
        return self.nom

class Message(models.Model):
    auteur = models.ForeignKey(User, related_name="auteur_message", on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name="salon")
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.auteur.username
