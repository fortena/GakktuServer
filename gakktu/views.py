from django.shortcuts import render
#from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .models import (Gender, Country, Language, Credential, Person,
                     Category, Article)
from .serializers import (UserSerializer, GroupSerializer, GenderSerializer, CountrySerializer, LanguageSerializer,
                          CredentialSerializer, PersonSerializer, CategorySerializer, ArticleSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GenderList(generics.ListCreateAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class GenderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class CredentialList(generics.ListCreateAPIView):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer


class CredentialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #permission_classes = (IsAuthenticated,)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


#class ArticleCommentList(generics.ListCreateAPIView):
#    queryset = ArticleComment.objects.all()
#    serializer_class = ArticleCommentSerializer


#class ArticleCommentDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = ArticleComment.objects.all()
#    serializer_class = ArticleCommentSerializer


#class ThreadList(generics.ListCreateAPIView):
#    queryset = Thread.objects.all()
#    serializer_class = ThreadSerializer


#class ThreadDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Thread.objects.all()
#    serializer_class = ThreadSerializer


#class ThreadCommentList(generics.ListCreateAPIView):
#    queryset = ThreadComment.objects.all()
#    serializer_class = ThreadCommentSerializer


#class ThreadCommentDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = ThreadComment.objects.all()
#    serializer_class = ThreadCommentSerializer
