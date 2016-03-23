from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.mixins import ListModelMixin
from drf_haystack.generics import HaystackGenericAPIView
from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.filters import HaystackAutocompleteFilter
from users.serializers import UserSearchSerializer
from users.search_indexes import UserIndex


class UserSearchView(HaystackViewSet):

	index_models = [User]
	serializer_class = UserSearchSerializer
	#filter_backends = [HaystackAutocompleteFilter]