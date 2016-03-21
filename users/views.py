from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.mixins import ListModelMixin
from drf_haystack.generics import HaystackGenericAPIView
from drf_haystack.viewsets import HaystackViewSet
from users.serializers import UserSearchSerializer
from users.search_indexes import UserIndex


class UserSearchView(ListModelMixin, HaystackGenericAPIView):

	serializer_class = UserSearchSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)