# -*- coding: utf-8 -*-
# @Date    : 27-03-2021
# @Author  : Hitesh Gorana
# @Link    : None
# @Version : 0.0
import datetime

from mongoengine import Document, connect, IntField, StringField, DateTimeField, ListField

connect('v002', host='127.0.0.1', port=27017)


class Song(Document):
    ID = IntField(required=True, unique=True)
    name = StringField(required=True, max_length=100)
    seconds = IntField(required=True, min_value=0)
    uploaded_time = DateTimeField(default=datetime.datetime.now)
    meta = dict(allow_inheritance=True)


class Podcast(Song):
    host = StringField(required=True, max_length=100)
    participants = ListField(max_length=10)


class Audiobook(Song):
    author = StringField(required=True, max_length=100)
    narrator = StringField(required=True, max_length=100)
