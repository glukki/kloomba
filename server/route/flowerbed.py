# coding=utf-8
from main import ProtobufHandler, DEBUG
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

        if DEBUG:
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
        r = FlowerbedAdd()

        if DEBUG:
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())


class FlowerbedTransferHandler(ProtobufHandler):
    """
    ancestor: tile
    request: /flowerbed/transfer?id=1&amount=1&direction=to
    response: State(Flowerbed, User)
    """
    def get(self):
        r = FlowerbedTransfer()

        if DEBUG:
            self.response.out.write(r)
        else:
            self.response.out.write(r.SerializeToString())
