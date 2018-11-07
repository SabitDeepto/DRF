from rest_framework import viewsets

from test_blog.models import Post
from test_blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
