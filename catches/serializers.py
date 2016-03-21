from rest_framework import serializers
from catches.models import Catch, Like
from comments.serializers import CommentSerializer
from django.contrib.auth.models import User
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
import pdb

#Haystack
from drf_haystack.serializers import HaystackSerializer
from catches.search_indexes import CatchIndex


class OwnerSerializer(serializers.RelatedField):
	def to_representation(self, value):
		return {'id':value.id, 'username': value.username}

class CatchSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
	owner = OwnerSerializer(read_only=True)
	liked = serializers.SerializerMethodField('is_liked')
	comments = CommentSerializer(many=True, read_only=True)
	tags = TagListSerializerField(required=False)
	
	class Meta:
		model = Catch
		fields = ('url', 'id', 'title', 'location', 'created_at', 'modified_at','liked', 'likes', 'tags', 'owner', 'length', 'fishPhoto', 'comments')
		read_only_fields = ('comments','owner',)
		
	def is_liked(self, obj):
		return (obj.liked_users.filter(user=self.context['request'].user).exists())
		
		
class LikeSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Like
		fields = ('user','catch')
		
class CatchSearchSerializer(HaystackSerializer):
	
	obj_id = serializers.SerializerMethodField('get_obj')	

	class Meta:
		index_classes = [CatchIndex]
		fields = ('text', 'owner', 'title', 'obj_id')
		
	def get_obj(self, obj):
		#pdb.set_trace()
		return (obj.pk)