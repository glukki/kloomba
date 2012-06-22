# coding=utf-8
from google.appengine.ext.db import GqlQuery
from google.appengine.api import memcache
from main import ProtobufHandler
import kloombaDb

__author__ = 'Vitaliy (GLuKKi) Meshchaninov glukki.spb.ru@gmail.com'


class UpdateHandler(ProtobufHandler):
    def get(self, table):
        if table in dir(kloombaDb):
            i = 0
            request = GqlQuery('SELECT * FROM ' + table).run()
            for item in request:
                i += 1
                if 'timestamp' in dir(item):
                    kloombaDb.__dict__[table].__dict__['timestamp'].__dict__['auto_now'] = False
                if 'lastActiveTimestamp' in dir(item):
                    kloombaDb.__dict__[table].__dict__['lastActiveTimestamp'].__dict__['auto_now'] = False
                item.put()
            memcache.flush_all()

            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write("Updated table: %s\nUpdated entitys: %d" % (table, i))