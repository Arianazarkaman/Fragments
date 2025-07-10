from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name','last_name', 'email', 'password', 'password2', 'is_staff']

    def validate(self, attrs):
        if attrs['password2'] != attrs['password']:
            raise serializers.ValidationError({'password': "password must match"})


        return attrs
    
    def create(self, validated_data):
        validated_data.pop("password2")
        user = get_user_model().objects.create_user(**validated_data)
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only = True)
    password = serializers.CharField(write_only = True)

    def validate(self, attrs):
        user = authenticate(username = attrs['username'], password = attrs['password'])
        if user is None:
            raise serializers.ValidationError("there's no user")
        else:
            attrs['user'] = user
            return attrs




 

