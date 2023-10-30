from rest_framework import serializers
from app.models import Customer
from app.models import Student


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'