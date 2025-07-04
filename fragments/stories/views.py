from django.shortcuts import render
from .models import Story, Page, Option
from django.shortcuts import get_object_or_404, redirect

def fragments(request):
    from django.contrib.auth.models import User
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "clear321")
    stories = Story.objects.all()
    return render(request, 'stories/home.html', {'stories': stories})

def story_start(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    
    first_page = Page.objects.filter(story=story).order_by('id').first()
    
    if first_page:
        return redirect('page_detail', page_id=first_page.id)
    else:
        return redirect('home')
    
def page_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    options = Option.objects.filter(page=page).order_by('id')
    context = {
        'page': page,
        'options': options,
    }
    return render(request, 'stories/page_detail.html', context)

