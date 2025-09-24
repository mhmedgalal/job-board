from .models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User

class ProfileSerializers(serializers.ModelSerializer):
     class Meta:
        model = Profile
        fields  = '__all__'

class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')
      
        extra_kwargs = {
            'username': {'required': True, 'allow_blank': False},
            'first_name': {'required': True, 'allow_blank': False}, 
            'last_name': {'required': True, 'allow_blank': False}, 
            'email': {'required': True, 'allow_blank': False}, 
            'password': {'required': True, 'allow_blank': False, 'min_length': 8, 'write_only': True}, 
        }


    def validate_email(self, value):
  
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value    


        
    def create(self, validated_data):
        # نعمل User object جديد
        user = User(
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', '')
        )
        # نعمل set للباسورد
        user.set_password(validated_data['password'])
        user.save()
        return user

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')