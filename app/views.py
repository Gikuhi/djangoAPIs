from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from app.models import Customer
from app.models import Student
from app.serializer import CustomerSerializer
from app.serializer import StudentSerializer
from rest_framework import viewsets

# Create your views here.

# def customer(request):
#     data = Customer.objects.all()
#     serializer = CustomerSerializer(data, many=True)
#     return JsonResponse({'customers': serializer.data})


class customerview(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class studentview(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer