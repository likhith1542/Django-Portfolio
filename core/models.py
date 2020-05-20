from django.db import models


#about model
from django import forms


class About(models.Model):
    short_description=models.TextField()
    description=models.TextField()
    image=models.ImageField(upload_to="about")

    class Meta:
        verbose_name="About me"
        verbose_name_plural="about me"

    def __str__(self):
        return "About me"



#service model
class Service(models.Model):
    name=models.CharField(max_length=100,verbose_name="Service name")
    description=models.TextField(verbose_name="About service")
    image=models.ImageField(upload_to="stuff",default="default.png")

    def __str__(self):
        return self.name

#recent work model
class Recentwork(models.Model):
    title=models.CharField(max_length=100,verbose_name="work title")
    image=models.ImageField(upload_to="works")

    def __str__(self):
        return self.title

#client model
class Client(models.Model):
    name=models.CharField(max_length=100,verbose_name="Client name")
    description=models.TextField(verbose_name="Client say")
    image=models.ImageField(upload_to="clients",default="default.png")

    def __str__(self):
        return self.name

class contact(models.Model):
    name=models.CharField(max_length=100)
    emailid=models.EmailField(max_length=50)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name