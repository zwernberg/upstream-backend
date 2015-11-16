from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from api.models import Catch
from api.serializers import CatchSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
	queryset = Catch.objects.all()
	serializer_class = CatchSerializer
	#permission_class = (permissions.IsAuthenticatedOrReadOnly)	
	
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)