from dataclasses import field, fields
from pyexpat import model
from turtle import update
from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","password"]
        extra_kwargs = {"password":{"write_only": True,"required":True }}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
    
class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M",read_only=True)
    update_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M",read_only=True)

    class Meta:
        model = Task
        fields = ["id","title","created_at","update_at"]