from .models import Story, Page, Option
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from .serializers import StorySerializer, PageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication



class Fragments(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Story.objects.all()
        serializer = StorySerializer(queryset, many = True)
        return Response(serializer.data)
    


class StoryStart(APIView):
    permission_classes = [AllowAny]

    def get(self, request, story_id):
        story = get_object_or_404(Story, id=story_id)

        first_page = Page.objects.filter(story=story).order_by('order').first()

        if not first_page:
            return Response({"detail": "No pages found for this story."}, status=status.HTTP_204_NO_CONTENT)

        serializer = PageSerializer(first_page)

        return Response(serializer.data)
    
class PageDetail(APIView):

    permission_classes = [AllowAny]

    def get(self, request, page_id):
        page = get_object_or_404(Page, id=page_id)
        options = Option.objects.filter(page=page).order_by('id')
        serializer = PageSerializer(page)

        return Response(serializer.data)
