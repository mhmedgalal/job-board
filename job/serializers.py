from rest_framework import serializers
from .models import Category,Job,Apply

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  = '__all__'

class JobSerializer(serializers.ModelSerializer):
     category = serializers.SlugRelatedField(
    queryset=Category.objects.all(),
    slug_field="name"
)
     class Meta:
        model = Job
        exclude  = ["slug","owner"]


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        exclude  = ["created_at"]