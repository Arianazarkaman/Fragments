from django.urls import path, include
from .views import SkillView, CertificateView
urlpatterns = [
    path('skills/', SkillView.as_view(), name="user_progress_get"),
    path('certificates/', CertificateView.as_view(), name='user_progress_post'),
]
