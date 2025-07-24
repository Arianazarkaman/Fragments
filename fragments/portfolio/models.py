from django.db import models

class Skill(models.Model):

    name = models.CharField(max_length=200)
    level = models.IntegerField()

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    def __str__(self):
        return self.name
    
class Certificate(models.Model):

    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='certificates/')
    link = models.URLField(max_length=300, blank=True)

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        return self.title