# coding=utf-8
import time
import hashlib
from google.appengine.api import users
from google.appengine.ext.db import Key
from main import ProtobufHandler, SALT, TICK, FLOWERS_PER_TICK, ACTION_DISTANCE, OBJECT_DISTANCE
import kloombaDb
from message.Login_pb2 import Login

__author__ = 'Vitaliy (GLuKKi) Meshchaninov glukki.spb.ru@gmail.com'

class LoginHandler(ProtobufHandler):
    """
    request: /login?ts=1
    response: User, Rule[], FirstTimeLogin
    """
    def get(self):
        r = Login()

        user = users.get_current_user()
        gamer_key = Key.from_path(kloombaDb.Gamer.kind(), user.user_id())
        gamer = kloombaDb.Gamer.all().ancestor(gamer_key).get()
        if not gamer:
            #make new account
            gamer = kloombaDb.Gamer(parent=gamer_key)
            gamer.user_id = user.user_id()
            gamer.public_id = hashlib.md5(user.user_id() + SALT).hexdigest()
            gamer.name = user.nickname()
            gamer.put()
            #make new backpack
            backpack = []
            #add flowers
            bp = kloombaDb.Backpack(parent=gamer_key)
            bp.owner = user.user_id()
            bp.name = 'flower'
            bp.amount = 100
            bp.put()
            backpack.append(bp)
            #add flowerbeds
            bp = kloombaDb.Backpack(parent=gamer_key)
            bp.owner = user.user_id()
            bp.name = 'flowerbed'
            bp.amount = 100
            bp.put()
            backpack.append(bp)
            #set first_time
            r.first_time = True
        else:
            gamer.put()
            backpack = kloombaDb.Backpack.all().ancestor(gamer_key).run()


        #set user
        r.user.timestamp = int(time.mktime(gamer.lastActiveTimestamp.timetuple()))
        r.user.id = gamer.public_id
        r.user.name = gamer.name
        r.user.level = gamer.level
        r.user.experience = gamer.experience
        #set backpack
        r.user.backpack.timestamp = int(time.time())
        for i in backpack:
            bp = r.user.backpack.item.add()
            bp.name = i.name
            bp.amount = i.amount


        #TODO: replace with rules update timestamp
        #TODO: always return rules
        if True or int(self.request.get('ts', 0)) < 1339610761:
            #set rules
            r.rules.timestamp = 1339610761
            rule = r.rules.item.add()
            rule.name = 'TICK'
            rule.value = str(TICK)
            rule = r.rules.item.add()
            rule.name = 'FLOWERS_PER_TICK'
            rule.value = str(FLOWERS_PER_TICK)
            rule = r.rules.item.add()
            rule.name = 'ACTION_DISTANCE'
            rule.value = str(ACTION_DISTANCE)
            rule = r.rules.item.add()
            rule.name = 'OBJECT_DISTANCE'
            rule.value = str(OBJECT_DISTANCE)

        if self.request.get('debug', False):
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())
