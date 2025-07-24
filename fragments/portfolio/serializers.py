from rest_framework import serializers
from .models import Skill, Certificate
from django.utils import translation


class SkillSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_lang(self):
        request = self.context.get('request')
        if request:
            path = request.path  
            lang = path.split('/')[1] if len(path.split('/')) > 1 else 'en'
            if lang in ['fa', 'en']:
                return lang
            return translation.get_language()
        return 'en'
    
    def get_name(self, obj):
        lang = self.get_lang()
        return getattr(obj, f"name_{lang}", obj.name)
    
    class Meta:
        model = Skill
        fields = ['name', 'level']


class CertificateSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

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

    def get_image(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url

    class Meta:
        model = Certificate
        fields = ['title', 'image', 'link']

