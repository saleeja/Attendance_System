from rest_framework import serializers
from .models import User, Worker

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', "username",'first_name','last_name' ,'email', 'position', 'address', 'phone_number']

class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ['user', 'attendance_status']
