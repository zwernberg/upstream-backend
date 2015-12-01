from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser


from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager

from django.shortcuts import render_to_response, render, get_object_or_404,\
    redirect

from api.models import Catch
from api.serializers import CatchSerializer


class CatchViewSet(viewsets.ModelViewSet):
	queryset = Catch.objects.all()
	serializer_class = CatchSerializer
	parser_classes = (MultiPartParser, FormParser,)
	#permission_class = (permissions.IsAuthenticatedOrReadOnly)	
	
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user, fishPhoto=self.request.data.get('fishPhoto'))


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