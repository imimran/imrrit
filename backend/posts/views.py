from django.shortcuts import render
from  rest_framework import generics, permissions
from .models import  Post, Vote
from .serializers import PostSerializer, VoteSerializer
# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes =  [permissions.IsAuthenticatedOrReadOnly]

    def  perform_create(self, serializer):
        serializer.save(author =  self.request.user)

class VoteCreate(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes =  [permissions.IsAuthenticated]   

    def get_queryset(self):
        user =self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.object.filter(voter = user, post=post)


    def perform_create(self, serializer):
        serializer.save(voter = self.request.user, post = Post.objects.get(pk=self.kwargs['pk']) )    
    
