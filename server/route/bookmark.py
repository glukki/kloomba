# coding=utf-8
import time
from google.appengine.api import users
from google.appengine.ext.db import Key
import kloombaDb
from main import ProtobufHandler, DEBUG
from message.BookmarkAdd_pb2 import BookmarkAdd
from message.BookmarkList_pb2 import BookmarkList
from message.BookmarkRemove_pb2 import BookmarkRemove

__author__ = 'Vitaliy (GLuKKi) Meshchaninov glukki.spb.ru@gmail.com'

class BookmarkListHandler(ProtobufHandler):
    """
    ancestor: user
    request: /bookmark/list
    response: Flowerbed[ ]
    """
    def get(self):
        r = BookmarkList()
        keys = []

        user = users.get_current_user()
        gamer_key = Key.from_path(kloombaDb.Gamer.kind(), user.user_id())
        bookmarks = kloombaDb.Bookmark.all().ancestor(gamer_key).run()
        r.timestamp = int(time.time())
        for i in bookmarks:
            keys.append(i.flowerbed.key())

        flowerbeds = kloombaDb.Flowerbed.get(keys) if keys else []
        for i in flowerbeds:
            fb = r.flowerbed.add()
            fb.timestamp = int(time.mktime(i.timestamp.timetuple()))
            fb.id = str(i.key())
            fb.latitude = int(i.point.lat * 1000000)
            fb.longitude = int(i.point.lon * 1000000)
            fb.owner = i.owner_public_id
            fb.flowers = i.flowers


        if self.request.get('debug', False):
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())


class BookmarkAddHandler(ProtobufHandler):
    """
    ancestor: user
    request: /bookmark/add?id=1
    response: State(?)
    """
    def get(self):
        r = BookmarkAdd()

        if not self.request.get('id'):
            return

        fb_key = self.request.get('id')
        user = users.get_current_user()
        gamer_key = Key.from_path(kloombaDb.Gamer.kind(), user.user_id())

        #get flowerbed
        flowerbed = kloombaDb.Flowerbed.get(fb_key)
        if not flowerbed:
            return #no such flowerbed
        #check bookmark
        bookmark = kloombaDb.Bookmark.all().ancestor(gamer_key).filter('flowerbed =', Key(fb_key)).get()
        if bookmark:
            return #bookmark allready exist

        bookmark = kloombaDb.Bookmark(parent=gamer_key)
        bookmark.owner = user.user_id()
        bookmark.flowerbed = flowerbed
        bookmark.put()

        r.timestamp = int(time.time())
        fb = r.flowerbed
        fb.timestamp = int(time.mktime(flowerbed.timestamp.timetuple()))
        fb.id = str(flowerbed.key())
        fb.latitude = int(flowerbed.point.lat * 1000000)
        fb.longitude = int(flowerbed.point.lon * 1000000)
        fb.owner = flowerbed.owner_public_id
        fb.flowers = flowerbed.flowers

        if self.request.get('debug', False):
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())


class BookmarkRemoveHandler(ProtobufHandler):
    """
    ancestor: user
    request: /bookmark/remove?id=1
    response: State(?)
    """
    def get(self):
        r = BookmarkRemove()

        if not self.request.get('id'):
            return

        fb_key = self.request.get('id')
        user = users.get_current_user()
        gamer_key = Key.from_path(kloombaDb.Gamer.kind(), user.user_id())

        #get bookmark
        bookmarks = kloombaDb.Bookmark.all().ancestor(gamer_key).run()
        bookmark = None
        for i in bookmarks:
            if str(i.flowerbed.key()) == fb_key:
                bookmark = i
                break

        if not bookmark:
            return

        bookmark.delete()

        r.timestamp = int(time.time())
        r.id = fb_key

        if self.request.get('debug', False):
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())
