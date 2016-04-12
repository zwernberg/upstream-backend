"""upstream URL Configuration"""

from api import views as apiViews
from catches import views as catchViews
from users import views as userViews
from comments.views import CommentViewSet
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as authViews
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from allauth.account import views as allauthViews

router = DefaultRouter(trailing_slash=False)
router.register(r'catches', catchViews.CatchViewSet)
router.register(r'feed', catchViews.FeedViewSet,base_name='feed')
router.register(r'users', apiViews.UserViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'search', userViews.UserSearchView, base_name='user-search')

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api/api-auth/', include('rest_framework.urls', 
	namespace='rest_framework')),
	url(r'^api/rest-auth/', include('rest_auth.urls')),
	url(r'^api/catchsearch/', catchViews.SearchView.as_view()),
	#url(r'^api/rest-auth/registration/account-confirm-email/(?P<key>\w+)/$', allauthViews.confirm_email,name="account_confirm_email"),
    (r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
	url(r'^api/admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
