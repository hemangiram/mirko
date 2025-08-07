from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import InternetPlan, Subscription
from .serializers import InternetPlanSerializer, SubscriptionSerializer

#  Register New User (No Auth Required)
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        email = request.data.get('email', '')
        
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)
        
        User.objects.create_user(username=username, password=password, email=email)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

#  Internet Plans: List All or Create New
class InternetPlanView(generics.ListCreateAPIView):
    queryset = InternetPlan.objects.all()
    serializer_class = InternetPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

#  Internet Plan Detail (GET, PUT, DELETE)
class InternetPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InternetPlan.objects.all()
    serializer_class = InternetPlanSerializer
    permission_classes = [permissions.IsAuthenticated]

#  Subscriptions: List User's or Create New
class SubscriptionView(generics.ListCreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 

class SubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
