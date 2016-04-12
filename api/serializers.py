from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Follow
from catches.models import Catch
from catches.serializers import CatchSerializer
from comments.serializers import CommentSerializer

class UserModelSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ('id','username')


class UserSerializer(serializers.ModelSerializer):
	catches = CatchSerializer(many=True)
	is_following = serializers.SerializerMethodField('check_is_following')
	followers = serializers.SerializerMethodField('num_followers')
	following = serializers.SerializerMethodField('num_following')
	class Meta:
		model = User
		depth = 1
		fields = ('url', 'id' ,'username', 'userprofile', 'is_following', 'followers', 'following', 'catches')
		read_only_fields = ('userprofile', 'followers', 'following', 'is_following')
		
	def num_followers(self,obj):
		return (obj.followers.count())
		
	def num_following(self, obj):
		return (obj.friends.count())
	
	def check_is_following(self, obj):
		return (obj.followers.filter(user=self.context['request'].user).exists())		
		

		
		
class FollowSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Follow
		fields=('user','target')