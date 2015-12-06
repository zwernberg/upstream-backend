from rest_framework import serializers
from .models import Catch
from django.contrib.auth.models import User

class CatchSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Catch
		# fields = ('url', 'id', 'title', 'owner', 'fishPhoto')	
		
		
class CatchModelSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')	
	class Meta:
		model = Catch
		fields = ('id','title','owner', 'fishPhoto','created_at','modified_at')		
		
class UserSerializer(serializers.ModelSerializer):
	catches = CatchModelSerializer(many=True)

	class Meta:
		model = User
		fields = ('url', 'id' ,'username', 'catches')