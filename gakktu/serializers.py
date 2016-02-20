from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import (Gender, Country, Language, Credential, Person,
                     Category, Article, ArticleComment, Thread, ThreadComment)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = ('id', 'name')


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name')


class CredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credential
        fields = ('id', 'name')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'user', 'credential', 'birthDate', 'countryOfOrigin', 'languages', 'gender')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'category', 'language', 'content', 'author', 'originalDate', 'rating', 'numberOfRatings')


class ArticleCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticleComment
        fields = ('id', 'article', 'content', 'author', 'originalDate', 'rating', 'numberOfRatings')


class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thread
        fields = ('id', 'title', 'content', 'author', 'originalDate', 'rating', 'numberOfRatings')


class ThreadCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThreadComment
        fields = ('id', 'thread', 'content', 'author', 'originalDate', 'rating', 'numberOfRatings')