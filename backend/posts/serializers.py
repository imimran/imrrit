from rest_framework import serializers
from .models import  Post, Vote


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    author_id = serializers.ReadOnlyField(source = 'author.id')
    class Meta:
        model = Post
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']     