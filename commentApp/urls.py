from django.urls import path
from .views import PostsViewSet, CommentsViewSet

urlpatterns = [
    path('posts/', PostsViewSet.as_view({'get': 'list'}), name='posts'),
    path('comments/', CommentsViewSet.as_view({'get': 'list'}), name='comments')
]