from django.db import models
from django.contrib.auth.models import User


class Gender(models.Model):
    name = models.TextField()


class Country(models.Model):
    name = models.TextField()


class Language(models.Model):
    name = models.TextField()


class Credential(models.Model):
    name = models.TextField()


class Person(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User)
    credential = models.ForeignKey(Credential)
    birthDate = models.DateField()
    countryOfOrigin = models.ForeignKey(Country)
    languages = models.ManyToManyField(Language)
    gender = models.ForeignKey(Gender)


class Category(models.Model):
    name = models.TextField()


class Content(models.Model):
    content = models.TextField()
    author = models.TextField()
    originalDate = models.DateField()
    rating = models.IntegerField()
    numberOfRatings = models.IntegerField()


class Article(Content):
    title = models.TextField()
    category = models.ForeignKey(Category)
    language = models.ForeignKey(Language)


class ArticleComment(Content):
    Article = models.ForeignKey(Article)


class Thread(Content):
    title = models.TextField()


class ThreadComment(Content):
    Thread = models.ForeignKey(Thread)





