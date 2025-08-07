from django.contrib import admin
from .models import Contact,Service,PricingPlan


admin.site.register(Contact)
admin.site.register(Service)
admin.site.register(PricingPlan)