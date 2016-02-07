from rest_framework import serializers
from .models import Catch, Follow, Like
from django.contrib.auth.models import User
from comments.serializers import CommentSerializer

class UserModelSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ('id','username')


class CatchSerializer(serializers.HyperlinkedModelSerializer):
	owner = UserModelSerializer(required=False)
	liked = serializers.SerializerMethodField('is_liked')
	comments = CommentSerializer(many=True)
	class Meta:
		model = Catch
		fields = ('url', 'id', 'title', 'created_at', 'modified_at','liked', 'likes', 'comments','owner', 'fishPhoto')
		read_only_fields = ('comments',)
		
	def is_liked(self, obj):
		return (obj.liked_users.filter(user=self.context['request'].user).exists())
		
class UserSerializer(serializers.ModelSerializer):
	catches = CatchSerializer(many=True)
	following = serializers.SerializerMethodField('is_following')
	
	class Meta:
		model = User
		depth = 2
		fields = ('url', 'id' ,'username', 'following', 'catches')
		
	def followers(self,obj):
		return obj.followers_set.all()
	
	def is_following(self, obj):
		return (obj.followers.filter(user=self.context['request'].user).exists())		
		
class LikeSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Like
		fields = ('user','catch')
		
		
class FollowSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Follow
		fields=('user','target')