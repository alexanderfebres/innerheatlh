from asyncore import write
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'email',
            'is_staff',
            'is_superuser',
            'first_name',
            'last_name',
            'password'
        ]
