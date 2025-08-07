from django.urls import path
from .views import (
    RegisterView,
    InternetPlanView, InternetPlanDetailView,
    SubscriptionView, SubscriptionDetailView,
)

urlpatterns = [
    path('regis/', RegisterView.as_view()),

    path('plans/', InternetPlanView.as_view()),
    path('plans/<int:pk>/', InternetPlanDetailView.as_view()),

    path('subscriptions/', SubscriptionView.as_view()),
    path('subscriptions/<int:pk>/', SubscriptionDetailView.as_view()),
    
]
