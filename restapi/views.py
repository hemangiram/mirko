from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
from .models import Testimation
from .serializers import TestimationSerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

class TestimationListCreate(generics.ListCreateAPIView):
    queryset = Testimation.objects.all()
    serializer_class = TestimationSerializer

     
    def perform_create(self, serializer):
        name = self.request.data.get('name')
        desc = self.request.data.get('desc')

       
        if Testimation.objects.filter(name=name, desc=desc).exists():
            raise ValidationError("This testimonial already exists.")

        serializer.save()

class TestimationDetailsView(APIView):
    def get(self,request,pk):
        test = get_object_or_404(Testimation,pk=pk)
        serializer = TestimationSerializer(test)
        return Response(serializer.data)
    

    def put(self,request,pk):
        test = get_object_or_404(Testimation, pk=pk)
        serializer = TestimationSerializer(test,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_404_BAD_REQUEST)


    def delete(self,request,pk):
      test = get_object_or_404(Testimation, pk=pk)
      test.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

