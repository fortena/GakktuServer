from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import (Gender, Country, Language, Credential, Person,
                     Category, Article, UserProfile)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'avatar', 'languages')


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ('id', 'name')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name')


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ('id', 'name')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:

        user = UserSerializer(read_only=True)
        credential = CredentialSerializer(read_only=True)
        countryOfOrigin = CountrySerializer(read_only=True)
        languages = LanguageSerializer(read_only=True)
        gender = GenderSerializer(read_only=True)

        model = Person
        fields = ('id', 'name', 'user', 'credential', 'birthDate', 'countryOfOrigin', 'languages', 'gender')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


#class ArticleSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Article
#        fields = ('id', 'title', 'category', 'language', 'content', 'author', 'originalDate', 'rating', 'numberOfRatings')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'image', 'author', 'created_at',
            'updated_at')


#class ArticleCommentSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = ArticleComment
#        fields = ('id', 'article', 'content', 'author', 'originalDate', 'rating', 'numberOfRatings')


#class ThreadSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Thread
#        fields = ('id', 'title', 'content', 'author', 'originalDate', 'rating', 'numberOfRatings')


#class ThreadCommentSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = ThreadComment
#        fields = ('id', 'thread', 'content', 'author', 'originalDate', 'rating', 'numberOfRatings')
