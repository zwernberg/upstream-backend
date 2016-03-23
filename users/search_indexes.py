import datetime
from haystack import indexes
from django.contrib.auth.models import User

class UserIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.EdgeNgramField(document=True, use_template=False)
	username = indexes.CharField(model_attr='username')
	autocomplete = indexes.EdgeNgramField()

	def get_model(self):
		return User
		
	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.filter(date_joined__lte=datetime.datetime.now())