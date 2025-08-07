from django.contrib import admin

# Register your models here.
from .models import InternetPlan,Subscription


admin.site.register(InternetPlan)
admin.site.register(Subscription)