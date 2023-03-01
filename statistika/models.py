from django.db import models
from Asosiy.models import Mahsulot,Client,Ombor

class Statistika(models.Model):
    mahsulot=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    ombor=models.ForeignKey(Ombor,on_delete=models.CASCADE,null=True)
    miqdor=models.PositiveIntegerField()
    sana=models.DateTimeField()
    umumiy_suma=models.PositiveBigIntegerField()
    tolandi=models.PositiveBigIntegerField()
    nasiya=models.PositiveBigIntegerField()


