from django.db import models
from django.conf import settings

class Story(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    background = models.ImageField(upload_to='story_backgrounds/', null=True, blank=True)
    
    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"

    def __str__(self):
        return self.title

class Page(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.IntegerField(default=0)
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
    def __str__(self):
        return f"{self.story.title} - {self.title}"

class Option(models.Model):
    page = models.ForeignKey(Page, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    next_page = models.ForeignKey(Page, related_name='incoming_options', on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Option"
        verbose_name_plural = "Options"

    def __str__(self):
        return f"{self.page.title} -> {self.text} -> {self.next_page.title}"

class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    current_page = models.ForeignKey(Page, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "User Progress"
        verbose_name_plural = "User Progresses"

    def __str__(self):
        return f"{self.user.username} in '{self.story.title}' at Page {self.current_page.id}"


