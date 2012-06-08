# coding=utf-8
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

        if DEBUG:
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

        if DEBUG:
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

        if DEBUG:
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())
