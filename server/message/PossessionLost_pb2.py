# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.net.proto2.python.public import descriptor
from google.net.proto2.python.public import message
from google.net.proto2.python.public import reflection
from google.net.proto2.proto import descriptor_pb2
# @@protoc_insertion_point(imports)


import Flowerbed_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='PossessionLost.proto',
  package='',
  serialized_pb='\n\x14PossessionLost.proto\x1a\x0f\x46lowerbed.proto\"B\n\x0ePossessionLost\x12\x11\n\ttimestamp\x18\x01 \x01(\x05\x12\x1d\n\tflowerbed\x18\x02 \x03(\x0b\x32\n.FlowerbedB/\n\x18\x63om.kloomba.app.protobufB\x13PossessionLostProto')




_POSSESSIONLOST = descriptor.Descriptor(
  name='PossessionLost',
  full_name='PossessionLost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='timestamp', full_name='PossessionLost.timestamp', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='flowerbed', full_name='PossessionLost.flowerbed', index=1,
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
  serialized_start=41,
  serialized_end=107,
)

_POSSESSIONLOST.fields_by_name['flowerbed'].message_type = Flowerbed_pb2._FLOWERBED
DESCRIPTOR.message_types_by_name['PossessionLost'] = _POSSESSIONLOST

class PossessionLost(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _POSSESSIONLOST
  
  # @@protoc_insertion_point(class_scope:PossessionLost)

# @@protoc_insertion_point(module_scope)