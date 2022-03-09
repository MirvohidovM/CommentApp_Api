from rest_framework import serializers
from .models import Post, Comment

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    reply = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['post', 'author', 'text', 'created_at', 'updated_at', 'reply']

    def get_reply(self, obj):
        if obj.parent:
            return f'{obj.author.username}ning {obj.parent.author.username} kommentariyasiga bildirgan fikri' \
                   f'JAVOB:{obj.text}'
        return f'{obj.author.username} ning "{obj.post.title}" mavzusiga bildirgan fikriga ' \
               f'JAVOB:{obj.text}'

    def get_post(self, obj):
        return f'mavzu {obj.post}'

    def get_author(self, obj):
        return f'avtor {obj.author}'