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
	followers =	serializers.StringRelatedField(many=True)

	
	class Meta:
		model = User
		depth = 2
		fields = ('url', 'id' ,'username', 'catches', 'friends','followers')
		
	def followers(self,obj):
		return obj.followers_set.all()
		
		
class LikeSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Like
		fields = ('user','catch')