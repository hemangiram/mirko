from django.urls import path
from .views import TestimationListCreate,TestimationDetailsView


urlpatterns = [
    path('test',TestimationListCreate.as_view(),name='test'),
    path('testing/<int:pk>/',TestimationDetailsView.as_view(),name='test-detail')
]
