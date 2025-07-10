from rest_framework import serializers
from .models import Story,Page, Option, UserProgress

class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ['title','description', 'author', 'created_at']

class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = ['page','text', 'next_page']


class PageSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Page
        fields = ['story','title', 'content','order', 'options']


class UserProgressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProgress
        fields = ['title','description', 'author', 'created_at']




    