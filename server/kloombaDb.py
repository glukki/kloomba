# coding=utf-8
__author__ = 'Vitaliy (GLuKKi) Meshchaninov glukki.spb.ru@gmail.com'

from google.appengine.ext import db

#ancestor: user_id
class Gamer(db.Model):
    user_id = db.StringProperty()
    public_id = db.StringProperty() #md5 hash
    name = db.StringProperty()
    avatar = db.IntegerProperty()
    level = db.IntegerProperty(default=1)
    experience = db.IntegerProperty(default=0)
    point = db.GeoPtProperty()
    registrationTimestamp = db.DateTimeProperty(auto_now_add=True)
    lastActiveTimestamp = db.DateTimeProperty(auto_now=True)

#get surrounding flowerbeds
#ancestor: tile
class Flowerbed(db.Model):
    point = db.GeoPtProperty()
    tile = db.StringProperty()
    level = db.IntegerProperty(default=1)
    owner = db.StringProperty()
    owner_public_id = db.StringProperty()
    flowers = db.IntegerProperty(default=0)
    timestamp = db.DateTimeProperty(auto_now=True)

#ancestor: flowerbed
class FlowerbedLog(db.Model):
    flowerbed = db.ReferenceProperty(reference_class=Flowerbed)
    owner = db.StringProperty()
    attackPlants = db.IntegerProperty()
    defensePlants = db.IntegerProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)

#store users current and lost flowerbeds
#ancestor: user_id
#send diff time in seconds, how long ago it was lost
class Possession(db.Model):
    flowerbed = db.ReferenceProperty(reference_class=Flowerbed)
    lost = db.BooleanProperty(default=False)
    timestamp = db.DateTimeProperty(auto_now=True)

#ancestor: user_id
class Bookmark(db.Model):
    owner = db.StringProperty()
    flowerbed = db.ReferenceProperty(reference_class=Flowerbed)
    timestamp = db.DateTimeProperty(auto_now=True)

#ancestor: "rules"
#tick, plantPerTick, lostFlowerbedTimeout
class Rule(db.Model):
    name = db.StringProperty()
    value = db.IntegerProperty()
    timestamp = db.DateTimeProperty(auto_now=True)

#ancestor: "shop"
class Item(db.Model):
    name = db.StringProperty() #flower, flowerbed
    moneyPrice = db.IntegerProperty()
    flowerPrice = db.IntegerProperty()

#ancestor: user_id
class Backpack(db.Model):
    owner = db.StringProperty()
    name = db.StringProperty() #Item.name
    amount = db.IntegerProperty()
    timestamp = db.DateTimeProperty(auto_now=True)

