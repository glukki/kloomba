# coding=utf-8
__author__ = 'Vitaliy (GLuKKi) Meshchaninov glukki.spb.ru@gmail.com'

from google.appengine.ext import db

#ancestor: user
class Gamer(db.Model):
    user = db.UserProperty(auto_current_user_add=True)
    name = db.StringProperty()
    avatar = db.IntegerProperty()
    level = db.IntegerProperty()
    experience = db.IntegerProperty()
    registrationTimestamp = db.DateTimeProperty(auto_now_add=True)
    lastActiveTimestamp = db.DateTimeProperty(auto_now=True)

#get surrounding flowerbeds
#ancestor: tile
class Flowerbed(db.Model):
    latitude = db.GeoPtProperty()
    geohash = db.StringProperty()
    level = db.IntegerProperty()
    owner = db.UserProperty()
    plants = db.IntegerProperty()
    timestamp = db.DateTimeProperty()

#ancestor: flowerbed
class FlowerbedLog(db.Model):
    flowerbed = db.ReferenceProperty(reference_class=Flowerbed)
    owner = db.UserProperty()
    attackPlants = db.IntegerProperty()
    defensePlants = db.IntegerProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)

#store users current and lost flowerbeds
#ancestor: user
#send diff time in seconds, how long ago it was lost
class Possession(db.Model):
    flowerbed = db.ReferenceProperty(reference_class=Flowerbed)
    lost = db.BooleanProperty()
    expireTimestamp = db.DateTimeProperty()

#ancestor: user
class Bookmark(db.Model):
    owner = db.UserProperty()
    flowerbed = db.ReferenceProperty(reference_class=Flowerbed)
    timestamp = db.DateTimeProperty()

#ancestor: "rule"
#tick, plantPerTick, lostFlowerbedTimeout
class Rule(db.Model):
    name = db.StringProperty()
    value = db.IntegerProperty()
    timestamp = db.DateTimeProperty(auto_now=True)

class Item(db.Model):
    id = db.StringProperty()
    name = db.StringProperty()
    moneyPrice = db.IntegerProperty()
    flowerPrice = db.IntegerProperty()

#ancestor: user
class Backpack(db.Model):
    owner = db.UserProperty()
    item = db.ReferenceProperty(reference_class=Item)
    amount = db.IntegerProperty()

