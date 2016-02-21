from django.shortcuts import render
from rest_framework import permissions, renderers, viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from catches.models import Catch,Like
from catches.serializers import CatchSerializer, LikeSerializer
from comments.serializers import CommentSerializer
from api.permissions import IsOwnerOrReadOnly
from stream_django.feed_manager import feed_manager
# Create your views here.
class CatchViewSet(viewsets.ModelViewSet):

	queryset = Catch.objects.order_by('-created_at')
	#queryset = Catch.objects.order_by('-created_at').select_related('owner',).prefetch_related('comments')
	serializer_class = CatchSerializer
	parser_classes = (MultiPartParser, FormParser,JSONParser,)
	permission_classes = (IsOwnerOrReadOnly,)	
	
	
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user, fishPhoto=self.request.data.get('fishPhoto'))


	@detail_route(methods=['get','post'])
	def comments(self,request,pk):
		if request.method == 'GET':
			comments = self.get_object().comments
			serializer = CommentSerializer(comments, context={'request': request}, many=True)
			return Response(serializer.data)
		
		else:
			serializer = CommentSerializer(data=request.data)
			if serializer.is_valid():				
				serializer.save(owner=self.request.user, target=Catch.objects.get(id=pk))
				return Response(status=status.HTTP_204_NO_CONTENT)				
						
	@detail_route(methods=['post'])
	def like(self,request,pk):
		data = {'user':self.request.user.id, 'catch': pk}
		serializer = LikeSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			catch = Catch.objects.get(id=pk)
			catch.likes += 1
			catch.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
			
	@detail_route(methods=['post'])
	def unlike(self,request,pk):
		catch = Catch.objects.get(id=pk)
		if (catch.liked_users.filter(user=self.request.user).exists()):
			obj = Like.objects.get(user=self.request.user,catch=catch)
			obj.delete()
			catch.likes -= 1
			catch.save()
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(status=status.HTTP_400_BAD_REQUEST)
		

class FeedViewSet(viewsets.ModelViewSet):
	serializer_class = CatchSerializer
	parser_classes = (MultiPartParser, FormParser,)
	#permission_class = (permissions.IsAuthenticatedOrReadOnly)	
	
	def get_queryset(self):
		feeds = feed_manager.get_news_feeds(self.request.user.id)
		activities = feeds.get('flat').get()['results']
		id_list = [a['object'].split(':')[1] for a in activities]
		id_list = [int(id) for id in id_list]
		queryset = Catch.objects.filter(id__in=id_list)
		return queryset

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user, fishPhoto=self.request.data.get('fishPhoto'))