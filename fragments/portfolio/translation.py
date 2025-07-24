from modeltranslation.translator import register, TranslationOptions
from .models import Skill, Certificate

@register(Skill)
class SkillTranslation(TranslationOptions):
    fields = ['name']

@register(Certificate)
class CertificateTranslation(TranslationOptions):
    fields = ['title']