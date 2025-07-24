from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Skill, Certificate
from .serializers import SkillSerializer, CertificateSerializer

class SkillView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Skill.objects.all()
        serializer = SkillSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
class CertificateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Certificate.objects.all()
        serializer = CertificateSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
