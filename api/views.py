from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from api.models import Catch
from api.serializers import CatchSerializer

class CatchViewSet(viewsets.ModelViewSet):
	queryset = Catch.objects.all()
	serializer_class = CatchSerializer
	parser_classes = (MultiPartParser, FormParser,)
	#permission_class = (permissions.IsAuthenticatedOrReadOnly)	
	
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user, fishPhoto=self.request.data.get('fishPhoto'))