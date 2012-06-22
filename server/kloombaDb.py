# coding=utf-8
__author__ = 'Vitaliy (GLuKKi) Meshchaninov glukki.spb.ru@gmail.com'

from google.appengine.ext import db

#ancestor: user_id
class Gamer(db.Model):
    user_id = db.StringProperty()
    public_id = db.StringProperty() #md5 hash
    name = db.StringProperty(indexed=False)
    avatar = db.IntegerProperty(indexed=False)
    level = db.IntegerProperty(indexed=False, default=1)
    experience = db.IntegerProperty(indexed=False, default=0)
    point = db.GeoPtProperty(indexed=False)
    registrationTimestamp = db.DateTimeProperty(indexed=False, auto_now_add=True)
    lastActiveTimestamp = db.DateTimeProperty(indexed=False, auto_now=True)

#get surrounding flowerbeds
#ancestor: tile
class Flowerbed(db.Model):
    point = db.GeoPtProperty(indexed=False)
    tile = db.StringProperty(indexed=False)
    level = db.IntegerProperty(indexed=False, default=1)
    owner = db.StringProperty(indexed=False)
    owner_public_id = db.StringProperty(indexed=False)
    flowers = db.IntegerProperty(indexed=False, default=0)
    timestamp = db.DateTimeProperty(indexed=False, auto_now=True)

#ancestor: flowerbed
class FlowerbedLog(db.Model):
    flowerbed = db.ReferenceProperty(indexed=False, reference_class=Flowerbed)
    owner = db.StringProperty()
    attackPlants = db.IntegerProperty(indexed=False)
    defensePlants = db.IntegerProperty(indexed=False)
    timestamp = db.DateTimeProperty(auto_now=True)

#store users current and lost flowerbeds
#ancestor: user_id
#send diff time in seconds, how long ago it was lost
class Possession(db.Model):
    flowerbed = db.ReferenceProperty(reference_class=Flowerbed)
    lost = db.BooleanProperty(default=False)
    timestamp = db.DateTimeProperty(indexed=False, auto_now=True)

#ancestor: user_id
class Bookmark(db.Model):
    owner = db.StringProperty(indexed=False)
    flowerbed = db.ReferenceProperty(indexed=False, reference_class=Flowerbed)
    timestamp = db.DateTimeProperty(indexed=False, auto_now=True)

#ancestor: "rules"
#tick, plantPerTick, lostFlowerbedTimeout
class Rule(db.Model):
    name = db.StringProperty(indexed=False)
    value = db.IntegerProperty(indexed=False)
    timestamp = db.DateTimeProperty(indexed=False, auto_now=True)

#ancestor: "shop"
class Item(db.Model):
    name = db.StringProperty() #flower, flowerbed
    moneyPrice = db.IntegerProperty(indexed=False)
    flowerPrice = db.IntegerProperty(indexed=False)

#ancestor: user_id
class Backpack(db.Model):
    owner = db.StringProperty(indexed=False)
    name = db.StringProperty() #Item.name
    amount = db.IntegerProperty(indexed=False)
    timestamp = db.DateTimeProperty(indexed=False, auto_now=True)

