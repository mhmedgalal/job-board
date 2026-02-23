from rest_framework import serializers
from .models import Category,Job,Apply

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  = '__all__'

class JobSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Job
        fields = [
            'id',
            'owner',
            'title',
            'job_type',
            'description',
            'experience',
            'published_at',
            'vacancy',
            'salary',
            'category',
            'image',
        ]
        read_only_fields = ['id', 'owner', 'published_at']


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = [
            'id',
            'user',
            'job',
            'name',
            'email',
            'website',
            'cv',
            'cover_letter',
            'created_at',
        ]
        read_only_fields = ['id', 'user', 'created_at']
