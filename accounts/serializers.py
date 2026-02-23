from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Profile


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'username': {'required': False, 'allow_blank': True},
            'first_name': {'required': True, 'allow_blank': False},
            'last_name': {'required': True, 'allow_blank': False},
            'email': {'required': True, 'allow_blank': False},
            'password': {
                'required': True,
                'allow_blank': False,
                'min_length': 8,
                'write_only': True,
            },
        }

    def validate_email(self, value):
        email = value.strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError('This email is already in use.')
        return email

    def create(self, validated_data):
        email = validated_data.get('email', '').strip().lower()
        username = validated_data.get('username') or email
        return User.objects.create_user(
            username=username,
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=email,
            password=validated_data['password'],
        )


class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
