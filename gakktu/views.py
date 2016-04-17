from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from datetime import datetime
from .models import (Gender, Country, Language, Credential, Person,
                     Category, Article, UserProfile)
from .serializers import (UserSerializer, GroupSerializer, GenderSerializer, CountrySerializer, LanguageSerializer,
                          CredentialSerializer, PersonSerializer, CategorySerializer, ArticleSerializer, UserProfileSerializer)


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


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializers_class = UserProfileSerializer

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
    def create(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'image': request.data.get('image'),
            'author': self.request.user.id,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        serializer = ArticleSerializer(data=data)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        if serializer.is_valid():
            instance = serializer.save()
        else:
            print(serializer.errors)

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
