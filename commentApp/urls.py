from django.urls import path
from .views import PostsViewSet, CommentsViewSet, RegisterUserView, CommentCreateView, CommentUpdateView

urlpatterns = [
    path('posts/', PostsViewSet.as_view({'get': 'list'}), name='posts'),
    path('comments/', CommentsViewSet.as_view({'get': 'list'}), name='comments'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('postcomment/', CommentCreateView.as_view(), name='postcomment' ),
    path('putcomment/<int:pk>/', CommentUpdateView.as_view(), name='putcomment')
]