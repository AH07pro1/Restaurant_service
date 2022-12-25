from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'f_name',
            'l_name',
            'email',
            'role'
        ]
