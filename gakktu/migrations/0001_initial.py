# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('author', models.TextField()),
                ('originalDate', models.DateField()),
                ('rating', models.IntegerField()),
                ('numberOfRatings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('birthDate', models.DateField()),
                ('countryOfOrigin', models.ForeignKey(to='gakktu.Country')),
                ('credential', models.ForeignKey(to='gakktu.Credential')),
                ('gender', models.ForeignKey(to='gakktu.Gender')),
                ('languages', models.ManyToManyField(to='gakktu.Language')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gakktu.Content')),
                ('title', models.TextField()),
                ('category', models.ForeignKey(to='gakktu.Category')),
                ('language', models.ForeignKey(to='gakktu.Language')),
            ],
            bases=('gakktu.content',),
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gakktu.Content')),
                ('Article', models.ForeignKey(to='gakktu.Article')),
            ],
            bases=('gakktu.content',),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gakktu.Content')),
                ('title', models.TextField()),
            ],
            bases=('gakktu.content',),
        ),
        migrations.CreateModel(
            name='ThreadComment',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gakktu.Content')),
                ('Thread', models.ForeignKey(to='gakktu.Thread')),
            ],
            bases=('gakktu.content',),
        ),
    ]
