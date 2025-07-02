from django.contrib import admin
from .models import Story, Page, Option, UserProgress
from modeltranslation.admin import TranslationAdmin

@admin.register(Story)
class StoryAdmin(TranslationAdmin): 
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')

@admin.register(Page)
class PageAdmin(TranslationAdmin):  
    list_display = ('title', 'story')
    search_fields = ('title', 'story__title')

@admin.register(Option)
class OptionAdmin(TranslationAdmin):
    list_display = ('page', 'text', 'next_page')

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):  
    list_display = ('user', 'story', 'current_page', 'last_updated')
