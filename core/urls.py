"""squatbot URL Configuration"""

from api import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as authViews

from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

router = DefaultRouter(trailing_slash=False)
router.register(r'catches', views.CatchViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', 
	namespace='rest_framework')),
	url(r'^api-token-auth', authViews.obtain_auth_token)
)
