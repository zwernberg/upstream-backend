from rest_framework import serializers
from .models import Catch
from django.contrib.auth.models import User

class CatchSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Catch
		fields = ('url', 'id', 'title', 'owner')	