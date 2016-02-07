"""upstream URL Configuration"""

from api import views
from comments.views import CommentViewSet
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
router.register(r'comments', CommentViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api/api-auth/', include('rest_framework.urls', 
	namespace='rest_framework')),
	url(r'^api/rest-auth/', include('rest_auth.urls')),
    (r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/currentuser', views.CurrentUserView.as_view()),
	url(r'^api/admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
