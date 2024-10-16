from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content',  'created_at', 'updated_at']
