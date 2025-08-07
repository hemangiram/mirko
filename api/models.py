
from django.db import models
from django.contrib.auth.models import User

class InternetPlan(models.Model):
    name = models.CharField(max_length=100)
    speed = models.CharField(max_length=50)  # e.g., "100 Mbps"
    data_limit = models.CharField(max_length=50)  # e.g., "200 GB"
    price = models.DecimalField(max_digits=8, decimal_places=2)
    validity_days = models.IntegerField()  # e.g., 30

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(InternetPlan, on_delete=models.CASCADE)
    subscribed_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} subscribed to {self.plan.name}"
