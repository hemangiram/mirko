from rest_framework import serializers
from .models import InternetPlan, Subscription

class InternetPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternetPlan
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    plan_detail = InternetPlanSerializer(source='plan', read_only=True)

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'plan', 'plan_detail', 'subscribed_on', 'active']
        read_only_fields = ['user']
