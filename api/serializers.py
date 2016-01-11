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
		#fields = ('url', 'id', 'title', 'owner', 'fishPhoto')			
		
class UserSerializer(serializers.ModelSerializer):
	catches = CatchSerializer(many=True)
	#followers = UserModelSerializer(many=True)
	followers = serializers.SerializerMethodField()
	isFollowing = serializers.SerializerMethodField()
	
	class Meta:
		model = User
		depth = 2
		fields = ('url', 'id' ,'username', 'catches', 'friends')
		
	def followers(self,obj):
		return obj.followers_set.all()
		
	def isFollowing(self,obj):
		return self.request.user in obj.followers.followers
		
		
class LikeSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Like
		fields = ('user','catch')