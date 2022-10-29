from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from envios.models import Post
from envios.api.serializers import PostSerializer

class PostApiView(APIView):
    def get(self,request):
        serializer = PostSerializer(Post.objects.all(),many=True)
        print(serializer)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self,request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK,data=serializer.data)