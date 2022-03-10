from django.urls import path
from .views import PostsViewSet, CommentsViewSet,RegisterUserView

urlpatterns = [
    path('posts/', PostsViewSet.as_view({'get': 'list'}), name='posts'),
    path('comments/', CommentsViewSet.as_view({'get': 'list'}), name='comments'),
    path('register/', RegisterUserView.as_view(), name='register')
]