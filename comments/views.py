from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.shortcuts import render_to_response, render, get_object_or_404,\
    redirect
from .serializers import CommentSerializer
from .models import Comment
from api.permissions import IsOwnerOrReadOnly


# Create your views here.


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.order_by('-created_at')
	serializer_class = CommentSerializer
	permission_classes = (IsOwnerOrReadOnly,)	
	
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user, fishPhoto=self.request.data.get('fishPhoto'))