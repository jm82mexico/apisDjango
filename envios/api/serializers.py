from dataclasses import fields
from importlib.metadata import files
from rest_framework.serializers import ModelSerializer
from envios.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description','order','create_at')
        # exclude = ['id']
        # fields='__all__'