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
	following = serializers.SerializerMethodField('is_following')
	
	class Meta:
		model = User
		depth = 2
		fields = ('url', 'id' ,'username', 'following', 'catches')
		
	def followers(self,obj):
		return obj.followers_set.all()
	
	def is_following(self, obj):
		return (obj.followers.filter(user=self.context['request'].user).exists())		
		

		
		
class FollowSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Follow
		fields=('user','target')