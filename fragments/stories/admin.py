from django.contrib import admin
from .models import Story, Page, Option, UserProgress
from modeltranslation.admin import TranslationAdmin

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

class OptionInline(TranslationTabularInline):
    model = Option
    extra = 3  
    show_change_link = True  
    fk_name = 'page'

@admin.register(Story)
class StoryAdmin(TranslationAdmin): 
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')

@admin.register(Page)
class PageAdmin(TranslationAdmin):  
    list_display = ('title', 'story')
    search_fields = ('title', 'story__title')
    list_filter = ('story',)
    inlines = [OptionInline] 


@admin.register(Option)
class OptionAdmin(TranslationAdmin):
    list_display = ('page', 'text', 'next_page')

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):  
    list_display = ('user', 'story', 'current_page', 'last_updated')
