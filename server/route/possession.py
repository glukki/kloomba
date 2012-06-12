# coding=utf-8
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.db import Key
import time
import kloombaDb
from main import ProtobufHandler, LOST_FLOWERBED_TIMEOUT
from message.PossessionList_pb2 import PossessionList
from message.PossessionLost_pb2 import PossessionLost

__author__ = 'Vitaliy (GLuKKi) Meshchaninov glukki.spb.ru@gmail.com'

class PossessionListHandler(ProtobufHandler):
    """
    ancestor: user
    request: /possession/list
    response: Flowerbed[ ]
    """
    def get(self):
        r = PossessionList()
        keys = []

        user = users.get_current_user()
        gamer_key = Key.from_path(kloombaDb.Gamer.kind(), user.user_id())
        possessions = kloombaDb.Possession.all().ancestor(gamer_key).filter('lost =', False).run()
        r.timestamp = int(time.time())
        for i in possessions:
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

class PossessionLostHandler(ProtobufHandler):
    """
    ancestor: user
    request: /possession/lost
    response: Flowerbed[ ]
    """
    def get(self):
        r = PossessionLost()
        to_delete = []
        keys = []

        user = users.get_current_user()
        gamer_key = Key.from_path(kloombaDb.Gamer.kind(), user.user_id())
        possessions = kloombaDb.Possession.all().ancestor(gamer_key).filter('lost =', True).run()
        r.timestamp = int(time.time())
        for i in possessions:
            if int(time.time()) - int(time.mktime(i.timestamp.timetuple())) > LOST_FLOWERBED_TIMEOUT:
                to_delete.append(i.flowerbed.key())
            else:
                keys.append(i.flowerbed.key())

        deleted = db.delete_async(to_delete)

        flowerbeds = kloombaDb.Flowerbed.get(keys) if keys else []
        for i in flowerbeds:
            fb = r.flowerbed.add()
            fb.timestamp = int(time.mktime(i.timestamp.timetuple()))
            fb.id = str(i.key())
            fb.latitude = int(i.point.lat * 1000000)
            fb.longitude = int(i.point.lon * 1000000)
            fb.owner = i.owner_public_id
            fb.flowers = i.flowers

        deleted.get_result()

        if self.request.get('debug', False):
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())
