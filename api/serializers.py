from rest_framework import serializers
from .models import Catch, Follow, Like
from django.contrib.auth.models import User

class UserModelSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ('id','username')


class CatchSerializer(serializers.HyperlinkedModelSerializer):
	owner = UserModelSerializer(required=False)

	class Meta:
		model = Catch
		fields = ('url', 'id', 'title', 'created_at', 'modified_at', 'likes', 'owner', 'fishPhoto')
		

		
class UserSerializer(serializers.ModelSerializer):
	catches = CatchSerializer(many=True)
	#followers = UserModelSerializer(many=True)
	#followers =	serializers.StringRelatedField(many=True)
	following = serializers.SerializerMethodField('is_following')
	
	class Meta:
		model = User
		depth = 2
		fields = ('url', 'id' ,'username', 'catches', 'following')
		
	def followers(self,obj):
		return obj.followers_set.all()
	
	def is_following(self, obj):
		return (obj.followers.filter(user=self.context['request'].user).exists())		
		
class LikeSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Like
		fields = ('user','catch')