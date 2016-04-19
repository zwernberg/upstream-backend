from rest_framework import serializers
from catches.models import Catch, Like
from django.contrib.auth.models import User
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from rest_auth.serializers import UserDetailsSerializer
import pdb

#Haystack
from drf_haystack.serializers import HaystackSerializer
from users.search_indexes import UserIndex


class UserSerializer(UserDetailsSerializer):
	bio = serializers.CharField(source="userprofile.bio", required=False, allow_blank=True)
	
	class Meta(UserDetailsSerializer.Meta):
		fields = UserDetailsSerializer.Meta.fields + ('bio',)
		
	def update(self, instance, validated_data):
		profile_data = validated_data.pop('userprofile', {})
		bio = profile_data.get('bio')
		
		instance = super(UserSerializer, self).update(instance, validated_data)
		
		profile = instance.userprofile
		profile.bio = bio
		profile.save()
		return instance
	


class UserSearchSerializer(HaystackSerializer):
	
	obj_id = serializers.SerializerMethodField('get_obj')	

	class Meta: 
		index_classes = [UserIndex]
		fields = ('username', 'obj_id', 'autocomplete')
		ignore_fields = ('autocomplete',)
		field_aliases = {
		    "q": "autocomplete"
		}

		
	def get_obj(self, obj):
		#pdb.set_trace()
		return (obj.pk)