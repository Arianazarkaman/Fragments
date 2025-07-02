from modeltranslation.translator import register, TranslationOptions
from .models import Story, Page, Option

@register(Story)
class StoryTranslation(TranslationOptions):
    fields = ('title', 'description',)

@register(Page)
class PageTranslation(TranslationOptions):
    fields = ('title', 'content')
@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('text',)
