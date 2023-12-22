from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import RegisterLoginModel

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']

    def save(self, **kwargs):
        user = User.objects.create_user(
            username=self.validated_data['username'],
            password=self.validated_data['password']
        )
        user.save()
        token = Token.objects.create(user=user)

class User_detailSerializer(serializers.ModelSerializer) :
    class Meta:
        model=RegisterLoginModel
        fields='__all__'



