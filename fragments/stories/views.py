from .models import Story, Page, Option, UserProgress
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from .serializers import StorySerializer, PageSerializer, UserProgressSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from .premissions import IsPremiumUser

class Fragments(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsPremiumUser]

    def get(self, request):
        queryset = Story.objects.all()
        serializer = StorySerializer(queryset, many = True, context={'request': request})
        return Response(serializer.data)
    

class StoryStart(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsPremiumUser]

    def get(self, request, story_id):
        story = get_object_or_404(Story, id=story_id)

        first_page = Page.objects.filter(story=story).order_by('order').first()

        if not first_page:
            return Response({"detail": "No pages found for this story."}, status=status.HTTP_204_NO_CONTENT)

        serializer = PageSerializer(first_page,  context={'request': request})

        return Response(serializer.data)
    
class PageDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsPremiumUser]

    def get(self, request, page_id):
        page = get_object_or_404(Page, id=page_id)
        serializer = PageSerializer(page, context={'request': request})
        return Response(serializer.data)


class UserProgressView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsPremiumUser]

    def get(self, request, story_id):
        user = request.user
        story = get_object_or_404(Story, id=story_id)
        try:
            queryset = UserProgress.objects.get(user=user, story=story)
            serializer = UserProgressSerializer(queryset)
            return Response(serializer.data)
        except UserProgress.DoesNotExist:
            return Response({"detail": "No progress found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        story = request.data.get('story')
        current_page = request.data.get('current_page')
        serializer = UserProgressSerializer(data={"story": story, "current_page": current_page})
        if serializer.is_valid():
            user = request.user
            story = serializer.validated_data['story']

            try:
                progress = UserProgress.objects.get(user = user, story = story)
                progress.current_page = serializer.validated_data['current_page']
                progress.save()
                return Response(UserProgressSerializer(progress).data, status=200)
            except UserProgress.DoesNotExist:
                serializer.save(user=user)
                return Response(serializer.data, status=201)
            
        else:
            return Response(serializer.errors, status=400)
                

                