from django.contrib.auth.models import User
from django.db import models

class Ombor(models.Model):
    nom=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    tel=models.CharField(max_length=13)
    ism=models.CharField(max_length=50)
    manzil=models.CharField(max_length=100)
    def __str__(self):
        return self.nom
class Mahsulot(models.Model):
    nom=models.CharField(max_length=50)
    brend=models.CharField(max_length=50)
    narx=models.IntegerField()
    kelgan_sana=models.DateTimeField()
    miqdor=models.IntegerField()
    ulchov=models.CharField(max_length=50)
    ombor_fk=models.ForeignKey(Ombor,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
class Client(models.Model):
    ism=models.CharField(max_length=50)
    nom=models.CharField(max_length=50)
    manzil=models.CharField(max_length=100)
    tel = models.CharField(max_length=13)
    qarz=models.IntegerField()
    ombor_fk = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism
