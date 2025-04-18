# TODO:  Напишите свой вариант

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions, filters, mixins
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group, Follow
from .serializers import (
    PostSerializer, GroupSerializer,
    CommentSerializer, FollowSerializer
)
from .permissions import AuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly, )

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        post_id = self.kwargs['post_id']
        self.current_post = get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        return self.current_post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.current_post)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
