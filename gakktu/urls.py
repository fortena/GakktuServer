from django.conf.urls import url, include
from rest_framework import routers
from .views import (UserViewSet, GroupViewSet, GenderList, GenderDetail, CountryList, CountryDetail, LanguageList,
                    LanguageDetail, CredentialList, CredentialDetail, PersonList, PersonDetail, CategoryList,
                    CategoryDetail, ArticleList, ArticleDetail, ArticleCommentList, ArticleCommentDetail, ThreadList,
                    ThreadDetail, ThreadCommentList, ThreadCommentDetail)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^genders/$', GenderList.as_view()),
    url(r'^genders/(?P<pk>[0-9]+)/$', GenderDetail.as_view()),
    url(r'^countries/$', CountryList.as_view()),
    url(r'^countries/(?P<pk>[0-9]+)/$', CountryDetail.as_view()),
    url(r'^languages/$', LanguageList.as_view()),
    url(r'^languages/(?P<pk>[0-9]+)/$', LanguageDetail.as_view()),
    url(r'^credentials/$', CredentialList.as_view()),
    url(r'^credentials/(?P<pk>[0-9]+)/$', CredentialDetail.as_view()),
    url(r'^persons/$', PersonList.as_view()),
    url(r'^persons/(?P<pk>[0-9]+)/$', PersonDetail.as_view()),
    url(r'^categories/$', CategoryList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/$', CategoryDetail.as_view()),
    url(r'^articles/$', ArticleList.as_view()),
    url(r'^articles/(?P<pk>[0-9]+)/$', ArticleDetail.as_view()),
    url(r'^articlecomments/$', ArticleCommentList.as_view()),
    url(r'^articlecomments/(?P<pk>[0-9]+)/$', ArticleCommentDetail.as_view()),
    url(r'^threads/$', ThreadList.as_view()),
    url(r'^threads/(?P<pk>[0-9]+)/$', ThreadDetail.as_view()),
    url(r'^threadcomments/$', ThreadCommentList.as_view()),
    url(r'^threadcomments/(?P<pk>[0-9]+)/$', ThreadCommentDetail.as_view()),
]
