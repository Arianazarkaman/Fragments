from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Page(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.story.title} - {self.title}"

class Option(models.Model):
    page = models.ForeignKey(Page, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    next_page = models.ForeignKey(Page, related_name='incoming_options', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.page.title} -> {self.text} -> {self.next_page.title}"

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    current_page = models.ForeignKey(Page, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} in '{self.story.title}' at Page {self.current_page.id}"
