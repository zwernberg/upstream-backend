from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager
from django.shortcuts import render_to_response, render, get_object_or_404,\
    redirect
from api.models import Follow
from api.serializers import UserSerializer, FollowSerializer
from api.permissions import IsOwnerOrReadOnly
from rest_framework.request import Request


#upstream.comments
from comments.serializers import CommentSerializer
from comments.models import Comment



		
		
class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This endpoint presents the users in the system.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

	@detail_route(methods=['post'])
	def follow(self,request,pk):
		data = {'user':self.request.user.id, 'target': pk}
		serializer = FollowSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
			
	@detail_route(methods=['post'])			
	def unfollow(self,request,pk):
		data = {'user':self.request.user.id, 'target': pk}
		target = User.objects.get(id=pk)
		if (target.followers.filter(user=self.request.user).exists()):
			obj = Follow.objects.get(user=self.request.user,target=target)
			obj.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
