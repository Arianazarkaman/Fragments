from django.urls import path, include
from .views import Fragments, StoryStart, PageDetail, UserProgressView
urlpatterns = [
    path('', Fragments.as_view(),name='home'),
    path('story_start/<int:story_id>/', StoryStart.as_view(), name='story_start'),
    path('page_detail/<int:page_id>/', PageDetail.as_view(), name='page_detail'),
    path('userprogress/<int:story_id>/', UserProgressView.as_view(), name="user_progress_get"),
    path('userprogress/', UserProgressView.as_view(), name='user_progress_post'),
]

