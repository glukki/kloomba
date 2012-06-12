# coding=utf-8
import hashlib
from math import floor
import time
from google.appengine.ext.db import Key, GeoPt
from geo import geocell
from google.appengine.api import users
from main import ProtobufHandler, DEBUG, SALT, TICK, FLOWERS_PER_TICK, GEO_RESOLUTION
import kloombaDb
from message.FlowerbedAdd_pb2 import FlowerbedAdd
from message.FlowerbedExplore_pb2 import FlowerbedExplore
from message.FlowerbedTransfer_pb2 import FlowerbedTransfer

__author__ = 'Vitaliy (GLuKKi) Meshchaninov glukki.spb.ru@gmail.com'

class FlowerbedExploreHandler(ProtobufHandler):
    """
    ancestor: tile
    request: /flowerbed/explore?lat=59955835&lon=30328488
    response: Flowerbed[ ]
    """
    def get(self):
        r = FlowerbedExplore()

        user = users.get_current_user()
        gamer_key = Key.from_path(kloombaDb.Gamer.kind(), user.user_id())
        gamer = kloombaDb.Gamer.all().ancestor(gamer_key).get()

        if self.request.get('lat') and self.request.get('lon'):
            r.timestamp = int(time.time())
            lat = float(self.request.get('lat')) / 1000000
            lon = float(self.request.get('lon')) / 1000000
            gamer.point = GeoPt(lat, lon) #update user position
            #take adjacent tiles
            tiles = []
            requests = []
            tile = geocell.compute(GeoPt(lat, lon), GEO_RESOLUTION)
            tiles.append(tile)
            tiles.extend(geocell.all_adjacents(tile))
            kind = kloombaDb.Flowerbed.kind()
            #prepare async requests
            for i in tiles:
                request = kloombaDb.Flowerbed.all().ancestor(Key.from_path(kind, i)).run()
                requests.append(request)
            for i in requests:
                for j in i:
                    fb = r.flowerbed.add()
                    fb.timestamp = int(time.mktime(j.timestamp.timetuple()))
                    fb.id = str(j.key())
                    fb.latitude = int(j.point.lat * 1000000)
                    fb.longitude = int(j.point.lon * 1000000)
                    fb.owner = j.owner_public_id
                    fb.flowers = j.flowers

        gamer.put()

        if self.request.get('debug', False):
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())


class FlowerbedAddHandler(ProtobufHandler):
    """
    ancestor: tile
    request: /flowerbed/add?lat=59955835&lon=30328488
    response: State(Flowerbed, User)
    """
    def get(self):
        user = users.get_current_user()
        r = FlowerbedAdd()
        if self.request.get('lat') and self.request.get('lon'):
            #TODO: check if flowerbed is far enough from others
            #TODO: check if flowerbed is close enough to user
            lat = float(self.request.get('lat')) / 1000000
            lon = float(self.request.get('lon')) / 1000000
            gamer_key = Key.from_path(kloombaDb.Gamer.kind(), user.user_id())
            kloombaDb.Gamer.all().ancestor(gamer_key).get().put()
            gamer_hash = hashlib.md5(user.user_id() + SALT).hexdigest()
            r.timestamp = int(time.time())
            #get backpack
            bp_beds = kloombaDb.Backpack.all().ancestor(gamer_key).filter('name =', 'flowerbed').get()
            if bp_beds.amount:
                #lower backpack
                bp_beds.amount -= 1
                bp_beds.put()

                #add flowerbed
                point = GeoPt(lat, lon)
                cell = geocell.compute(point, GEO_RESOLUTION)
                flowerbed = kloombaDb.Flowerbed(parent=Key.from_path(kloombaDb.Flowerbed.kind(), cell))
                flowerbed.point = point
                flowerbed.tile = cell
                flowerbed.owner = user.user_id()
                flowerbed.owner_public_id = gamer_hash
                flowerbed.put()
                possession = kloombaDb.Possession(parent=gamer_key)
                possession.flowerbed = flowerbed
                possession.put()

                backpack = kloombaDb.Backpack.all().ancestor(gamer_key)

                #set timestamps
                r.flowerbed.timestamp = int(time.time())
                r.backpack.timestamp = int(time.time())

                #set flowerbed
                r.flowerbed.id = str(flowerbed.key())
                r.flowerbed.latitude = int(self.request.get('lat'))
                r.flowerbed.longitude = int(self.request.get('lon'))
                r.flowerbed.owner = gamer_hash
                r.flowerbed.flowers = 0

                #set backpack
                for i in backpack:
                    bp = r.backpack.item.add()
                    bp.name = i.name
                    bp.amount = i.amount


        if self.request.get('debug', False):
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())


class FlowerbedTransferHandler(ProtobufHandler):
    """
    ancestor: tile
    request: /flowerbed/transfer?id=1&amount=1
    response: State(Flowerbed, User)
    """
    def get(self):
        r = FlowerbedTransfer()

        if not int(self.request.get('amount'), 0):
            return

        fb_id = self.request.get('id')
        amount = int(self.request.get('amount'))


        flowerbed = kloombaDb.Flowerbed.get(fb_id)
        ts = time.time()
        if flowerbed:
            fb_flowers = flowerbed.flowers +\
                         int(floor(
                             (ts - time.mktime(flowerbed.timestamp.timetuple())) / TICK *\
                             FLOWERS_PER_TICK
                         ))
            user = users.get_current_user()
            gamer_key = Key.from_path(kloombaDb.Gamer.kind(), user.user_id())
            gamer_hash = hashlib.md5(user.user_id() + SALT).hexdigest()
            bp_flowers = kloombaDb.Backpack.all().ancestor(gamer_key).filter('name =', 'flower').get()
            kloombaDb.Gamer.all().ancestor(gamer_key).get().put()

            #TODO: check if flowerbed is close to user
            if amount < 0: #from
                if flowerbed.owner != user.user_id():
                    return #not your flowerbed
                if fb_flowers < amount * -1:
                    return #not enough on flowerbed
                #ok, now substract
                flowerbed.flowers = fb_flowers + amount
                flowerbed.put()
                bp_flowers.amount -= amount
                bp_flowers.put()
            else: #to
                if bp_flowers.amount < amount:
                    return #not enough in backpack
                if flowerbed.owner == user.user_id():
                    #ok, it's mine
                    flowerbed.flowers = fb_flowers + amount
                    flowerbed.put()
                    bp_flowers.amount -= amount
                    bp_flowers.put()
                else: #ok, attack
                    if fb_flowers - amount >= 0:
                        #still the same owner
                        flowerbed.flowers = fb_flowers - amount
                        flowerbed.put()
                        bp_flowers.amount -= amount
                        bp_flowers.put()
                    else: #conquer
                        #set lost
                        lost = kloombaDb.Possession.all().ancestor(Key.from_path(kloombaDb.Gamer.kind(), flowerbed.owner)).filter('flowerbed =', flowerbed).get()
                        lost.lost = True
                        lost.put()
                        #set flowerbed
                        flowerbed.flowers = fb_flowers - amount
                        flowerbed.owner = user.user_id()
                        flowerbed.owner_public_id = gamer_hash
                        flowerbed.put()
                        #set backpack
                        bp_flowers.amount -= amount
                        bp_flowers.put()
                        #set conquer
                        possession = kloombaDb.Possession.all().ancestor(gamer_key).filter('flowerbed =', flowerbed).get()
                        if not possession:
                            possession = kloombaDb.Possession()
                            possession.flowerbed = flowerbed
                        possession.lost = False
                        possession.put()

            backpack = kloombaDb.Backpack.all().ancestor(gamer_key)

            #set timestamps
            r.flowerbed.timestamp = int(time.time())
            r.backpack.timestamp = int(time.time())

            #set flowerbed
            r.flowerbed.id = str(flowerbed.key())
            r.flowerbed.latitude = int(flowerbed.point.lat * 1000000)
            r.flowerbed.longitude = int(flowerbed.point.lon * 1000000)
            r.flowerbed.owner = flowerbed.owner_public_id
            r.flowerbed.flowers = flowerbed.flowers

            #set backpack
            for i in backpack:
                bp = r.backpack.item.add()
                bp.name = i.name
                bp.amount = i.amount

        if self.request.get('debug', False):
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())
