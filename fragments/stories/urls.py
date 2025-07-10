from django.urls import path, include
from .views import Fragments, StoryStart, PageDetail
urlpatterns = [
    path('', Fragments.as_view(),name='home'),
    path('story_start/<int:story_id>/', StoryStart.as_view(), name='story_start'),
    path('page/<int:page_id>/', PageDetail.as_view(), name='page_detail'),
]

