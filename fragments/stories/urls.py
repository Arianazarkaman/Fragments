from django.urls import path
from . import views

urlpatterns = [
    path('', views.fragments,name='home'),
    path('story_start/<int:story_id>/', views.story_start, name='story_start'),
    path('page/<int:page_id>/', views.page_detail, name='page_detail'),
]

