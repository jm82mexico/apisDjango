from urllib import response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from envios.models import Post
from envios.api.serializers import PostSerializer

class PostModelViewSet(ModelViewSet):
   serializer_class = PostSerializer
   queryset = Post.objects.all()