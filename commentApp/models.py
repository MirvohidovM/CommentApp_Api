from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models

# {
# "username": "mirshohid",
# "password": "2183707uyim",
# "email": "mirshohid@gmail.com"
# }
# class User(AbstractUser, PermissionsMixin):
#     email = models.EmailField()
#     username = models.CharField(unique=True, max_length=25)
#     password = models.CharField(max_length=200)
#
#     def __str__(self):
#         return f'{self.username}'


class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    text = models.TextField()
    media = models.FileField(upload_to='mediaFile', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)

    def __str__(self):
        return f'{self.author.username} ning kommenti'

    class Meta:
        ordering = ('post',)