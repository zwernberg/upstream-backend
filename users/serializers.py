from rest_framework import serializers
from catches.models import Catch, Like
from django.contrib.auth.models import User
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
import pdb

#Haystack
from drf_haystack.serializers import HaystackSerializer
from users.search_indexes import UserIndex

class UserSearchSerializer(HaystackSerializer):
	
	obj_id = serializers.SerializerMethodField('get_obj')	

	class Meta:
		index_classes = [UserIndex]
		fields = ('username', 'obj_id')
		
	def get_obj(self, obj):
		#pdb.set_trace()
		return (obj.pk)