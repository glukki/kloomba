# coding=utf-8
import time
from google.appengine.api import users
from main import ProtobufHandler, DEBUG
import kloombaDb
from message.Login_pb2 import Login

__author__ = 'glukki'

class LoginHandler(ProtobufHandler):
    """
    request: /login?ts=1
    response: User, Rule[], FirstTimeLogin
    """
    def get(self):
        r = Login()

        user = users.get_current_user()
        q = kloombaDb.Gamer.all()
        q.filter('user =', user)
        gamer = q.fetch(1)
        if not gamer:
            #make new account
            gamer = kloombaDb.Gamer()
            gamer.name = user.nickname()
            gamer.level = 1
            gamer.experience = 0
            gamer.put()
            #set first_time
            r.first_time = True
        else:
            gamer = gamer[0]
            gamer.put()

        #set user
        r.user.name = gamer.name
        r.user.level = gamer.level
        r.user.experience = gamer.experience

        #TODO: replace with rules update timestamp
        if int(self.request.get('ts', 0)) < int(time.time()):
            #set rules
            rule = r.rules.item.add()
            rule.name = 'test'
            rule.value = 'val'

        if DEBUG:
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())
