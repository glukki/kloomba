# coding=utf-8
# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.net.proto2.python.public import descriptor
from google.net.proto2.python.public import message
from google.net.proto2.python.public import reflection
from google.net.proto2.proto import descriptor_pb2
# @@protoc_insertion_point(imports)


import Flowerbed_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='FlowerbedExplore.proto',
  package='',
  serialized_pb='\n\x16\x46lowerbedExplore.proto\x1a\x0f\x46lowerbed.proto\"D\n\x10\x46lowerbedExplore\x12\x11\n\ttimestamp\x18\x01 \x01(\x05\x12\x1d\n\tflowerbed\x18\x02 \x03(\x0b\x32\n.FlowerbedB5\n\x1c\x63om.kloomba.app.api.protobufB\x15\x46lowerbedExploreProto')




_FLOWERBEDEXPLORE = descriptor.Descriptor(
  name='FlowerbedExplore',
  full_name='FlowerbedExplore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='timestamp', full_name='FlowerbedExplore.timestamp', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='flowerbed', full_name='FlowerbedExplore.flowerbed', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=43,
  serialized_end=111,
)

_FLOWERBEDEXPLORE.fields_by_name['flowerbed'].message_type = Flowerbed_pb2._FLOWERBED
DESCRIPTOR.message_types_by_name['FlowerbedExplore'] = _FLOWERBEDEXPLORE

class FlowerbedExplore(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FLOWERBEDEXPLORE
  
  # @@protoc_insertion_point(class_scope:FlowerbedExplore)

# @@protoc_insertion_point(module_scope)
