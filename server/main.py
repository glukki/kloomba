# coding=utf-8
import os
import webapp2
from webapp2_extras import routes
from google.appengine.api import users

__author__ = 'Vitaliy (GLuKKi) Meshchaninov glukki.spb.ru@gmail.com'

DEBUG = True if 'Development' in os.environ.get('SERVER_SOFTWARE', '') else False
SALT = 'kloo'
GEO_RESOLUTION = 17
TICK = 60
FLOWERS_PER_TICK = 10
LOST_FLOWERBED_TIMEOUT = 7 * 24 * 60 * 60

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))
#            self.response.out.write(users.create_login_url("/login"))


class ProtobufHandler(webapp2.RequestHandler):
    def __init__(self, request=None, response=None):
        webapp2.RequestHandler.__init__(self, request, response)
        if DEBUG:
            self.response.headers['Content-type'] = 'text/plain'
        else:
            self.response.headers['Content-type'] = 'binary/octet-stream'


app = webapp2.WSGIApplication(
    [
        webapp2.Route('/', 'main.MainHandler'),
        webapp2.Route('/login', 'route.login.LoginHandler'),
        routes.PathPrefixRoute('/flowerbed', [
            webapp2.Route('/explore', 'route.flowerbed.FlowerbedExploreHandler'),
            webapp2.Route('/add', 'route.flowerbed.FlowerbedAddHandler'),
            webapp2.Route('/transfer', 'route.flowerbed.FlowerbedTransferHandler'),
        ]),
        routes.PathPrefixRoute('/possession', [
            webapp2.Route('/list', 'route.possession.PossessionListHandler'),
            webapp2.Route('/lost', 'route.possession.PossessionLostHandler'),
        ]),
        routes.PathPrefixRoute('/bookmark', [
            webapp2.Route('/list', 'route.bookmark.BookmarkListHandler'),
            webapp2.Route('/add', 'route.bookmark.BookmarkAddHandler'),
            webapp2.Route('/remove', 'route.bookmark.BookmarkRemoveHandler'),
        ]),
    ],debug=DEBUG)
