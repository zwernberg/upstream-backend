"""upstream URL Configuration"""

from api import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as authViews

from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter(trailing_slash=False)
router.register(r'catches', views.CatchViewSet)
router.register(r'feed',views.FeedViewSet,base_name='feed')
router.register(r'users', views.UserViewSet)


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', 
	namespace='rest_framework')),
	url(r'^api-token-auth', authViews.obtain_auth_token),
	url(r'^rest-auth/', include('rest_auth.urls')),
    (r'^rest-auth/registration', include('rest_auth.registration.urls')),
	url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
