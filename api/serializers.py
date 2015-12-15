from rest_framework import serializers
from .models import Catch, Follow
from django.contrib.auth.models import User

class UserModelSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ('id','username')


class CatchSerializer(serializers.HyperlinkedModelSerializer):
	owner = UserModelSerializer(required=False)

	class Meta:
		model = Catch
		fields = ('url', 'id', 'title', 'owner', 'fishPhoto')			
		
class UserSerializer(serializers.ModelSerializer):
	catches = CatchSerializer(many=True)
	#followers = UserModelSerializer(User.followers,many=True)
	
	class Meta:
		model = User
		fields = ('url', 'id' ,'username', 'catches', 'followers')