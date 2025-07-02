from django.shortcuts import render
from .models import Story, Page, Option
from django.shortcuts import get_object_or_404, redirect

def fragments(request):
    stories = Story.objects.all()
    print(f"Found stories count: {stories.count()}")
    return render(request, 'stories/home.html', {'stories': stories})

