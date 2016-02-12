from rest_framework import serializers
from catches.models import Catch, Like
from comments.serializers import CommentSerializer
from django.contrib.auth.models import User


class OwnerSerializer(serializers.RelatedField):
	def to_representation(self, value):
		return {'id':value.id, 'username': value.username}

class CatchSerializer(serializers.HyperlinkedModelSerializer):
	owner = OwnerSerializer(read_only=True)
	liked = serializers.SerializerMethodField('is_liked')
	comments = CommentSerializer(many=True, read_only=True)
	class Meta:
		model = Catch
		fields = ('url', 'id', 'title', 'created_at', 'modified_at','liked', 'likes', 'comments','owner', 'fishPhoto')
		read_only_fields = ('comments','owner',)
		
	def is_liked(self, obj):
		return (obj.liked_users.filter(user=self.context['request'].user).exists())
		
		
class LikeSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Like
		fields = ('user','catch')