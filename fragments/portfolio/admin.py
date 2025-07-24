from django.contrib import admin
from .models import Skill, Certificate

from modeltranslation.admin import TranslationAdmin

@admin.register(Skill)
class SkillAdmin(TranslationAdmin):
    list_display = ['name', 'level']
    search_fields = ['name']

@admin.register(Certificate)
class CertificateAdmin(TranslationAdmin):
    list_display = ['title', 'link']
    search_fields = ['title']

