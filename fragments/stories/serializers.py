from rest_framework import serializers
from .models import Story,Page, Option, UserProgress
from django.utils import translation

class StorySerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_lang(self):
        request = self.context.get('request')
        if request:
            # Option 1: get from path, e.g. /fa/api/
            path = request.path  # e.g. /fa/api/
            lang = path.split('/')[1] if len(path.split('/')) > 1 else 'en'
            if lang in ['fa', 'en']:
                return lang

            # Option 2: fallback to django's current language
            return translation.get_language()
        return 'en'

    def get_title(self, obj):
        lang = self.get_lang()
        return getattr(obj, f"title_{lang}", obj.title)

    def get_description(self, obj):
        lang = self.get_lang()
        return getattr(obj, f"description_{lang}", obj.description)

    class Meta:
        model = Story
        fields = ['id', 'title', 'description', 'author', 'created_at', 'background']

class OptionSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()
    next_page = serializers.PrimaryKeyRelatedField(read_only=True)

    def get_lang(self):
        request = self.context.get('request')
        if request:
            path = request.path
            lang = path.split('/')[1] if len(path.split('/')) > 1 else 'en'
            if lang in ['fa', 'en']:
                return lang
            return translation.get_language()
        return 'en'

    def get_text(self, obj):
        lang = self.get_lang()
        return getattr(obj, f"text_{lang}", obj.text)

    class Meta:
        model = Option
        fields = ['text', 'next_page']


class PageSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    options = OptionSerializer(many=True, read_only=True)
    background = serializers.SerializerMethodField()

    def get_lang(self):
        request = self.context.get('request')
        if request:
            path = request.path
            lang = path.split('/')[1] if len(path.split('/')) > 1 else 'en'
            if lang in ['fa', 'en']:
                return lang
            return translation.get_language()
        return 'en'

    def get_title(self, obj):
        lang = self.get_lang()
        return getattr(obj, f"title_{lang}", obj.title)

    def get_content(self, obj):
        lang = self.get_lang()
        return getattr(obj, f"content_{lang}", obj.content)

    def get_background(self, obj):
        request = self.context.get('request')
        if obj.story and obj.story.background and hasattr(obj.story.background, 'url'):
            return request.build_absolute_uri(obj.story.background.url)
        return None

    class Meta:
        model = Page
        fields = ['story', 'title', 'content', 'order', 'options', 'background']



class UserProgressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProgress
        fields = ['story','current_page', 'last_updated', 'user']
        read_only_fields = ['user']



    