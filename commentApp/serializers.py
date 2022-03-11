from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
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
                   f'REPLY:{obj.text}'
        return f'{obj.author.username} ning "{obj.post.title}" mavzusiga bildirgan fikri' \
               f'COMMENT:{obj.text}'

    def get_post(self, obj):
        return f'mavzu {obj.post}'

    def get_author(self, obj):
        return f'avtor {obj.author}'


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'min_length': 8},
        }

    def create(self, validated_data):
        user = self.Meta.model.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
