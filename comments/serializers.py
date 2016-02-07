from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User


class OwnerSerializer(serializers.RelatedField):
	def to_representation(self, value):
		return {'id':value.id, 'username': value.username}

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	owner = OwnerSerializer(read_only=True)
	
	class Meta:
		model = Comment
		fields = ('id', 'target', 'text', 'owner')