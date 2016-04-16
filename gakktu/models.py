from django.db import models
from django.contrib.auth.models import User


class Gender(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name


class Country(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name


class Language(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name


class Credential(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name


class Person(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User)
    credential = models.ForeignKey(Credential)
    birthDate = models.DateField()
    countryOfOrigin = models.ForeignKey(Country)
    languages = models.ManyToManyField(Language)
    gender = models.ForeignKey(Gender)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    languages = models.ManyToManyField(Language, blank=True)
    avatar = models.TextField(blank=True)


class Category(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name


#class Content(models.Model):
#    content = models.TextField()
#    author = models.ForeignKey(Person)
#    originalDate = models.DateField()
#    rating = models.IntegerField()
#    numberOfRatings = models.IntegerField()


#class Article(Content):
#    title = models.TextField()
#    category = models.ForeignKey(Category)
#    language = models.ForeignKey(Language)
#
#    def __unicode__(self):
#        return self.title


class Article(models.Model):
    title = models.TextField()
    content = models.TextField(default='Woops somebody forgot about me')
    image = models.TextField(default='http://www.liveinthegrey.com/wp-content/uploads/2015/12/used-100x100.jpg')


#class ArticleComment(Content):
#    Article = models.ForeignKey(Article)


#class Thread(Content):
#    title = models.TextField()


#class ThreadComment(Content):
#    Thread = models.ForeignKey(Thread)
