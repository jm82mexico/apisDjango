from urllib import response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from envios.models import Post
from envios.api.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

class PostModelViewSet(ModelViewSet):
   permission_classes=[IsAuthenticatedOrReadOnly]
   serializer_class = PostSerializer
   queryset = Post.objects.all()