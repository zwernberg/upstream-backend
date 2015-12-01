from rest_framework import serializers
from .models import Catch
from django.contrib.auth.models import User

class CatchSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Catch
		# fields = ('url', 'id', 'title', 'owner', 'fishPhoto')	
		
		
class UserSerializer(serializers.HyperlinkedModelSerializer):
    catches = serializers.HyperlinkedRelatedField(queryset=Catch.objects.all(), view_name='catch-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'catches', 'friends')