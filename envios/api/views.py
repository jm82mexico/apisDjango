from urllib import response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from envios.models import Post
from envios.api.serializers import PostSerializer

class PostViewSet(ViewSet):
    def list(self,request):
        serializer = PostSerializer(Post.objects.all(),many=True)        
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self,request, pk: int):
        post = PostSerializer(Post.objects.get(pk=pk))
        print(post.data)
        return Response(status=status.HTTP_200_OK, data=post.data)

    def create(self,request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK,data=serializer.data)