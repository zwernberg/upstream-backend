import datetime
from haystack import indexes
from catches.models import Catch

class CatchIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.EdgeNgramField(document=True, use_template=False)
	title = indexes.CharField(model_attr='title')
	owner = indexes.CharField(model_attr='owner')
	
	def get_model(self):
		return Catch
		
	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.filter(created_at__lte=datetime.datetime.now())