# coding=utf-8
from main import ProtobufHandler, DEBUG
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

        if DEBUG:
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

        if DEBUG:
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())
