from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ECGList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="ECGlist",null=True)
    name = models.CharField((""), max_length=200)

    def __str__(self):
        return self.name

class ECGdata(models.Model):
    ECGlist = models.ForeignKey(ECGList, on_delete = models.CASCADE)
    volt = models.CharField(max_length=10)
    nomal = models.BooleanField()
    time = models.DateTimeField(auto_now=True)
    abnomal = models.CharField(max_length=30)

    def __str__(self):
        return self.text