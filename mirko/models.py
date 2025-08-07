from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    message = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    icon_image = models.ImageField(upload_to='service_icons/', null=True, blank=True)


    def __str__(self):
        return self.name
    
class PricingPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    features = models.TextField(help_text="Use comma-separated features")
    price = models.CharField(max_length=50)


    def __str__(self):
        return self.title
    