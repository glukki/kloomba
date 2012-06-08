# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.net.proto2.python.public import descriptor
from google.net.proto2.python.public import message
from google.net.proto2.python.public import reflection
from google.net.proto2.proto import descriptor_pb2
# @@protoc_insertion_point(imports)


import User_pb2
import RuleList_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='Login.proto',
  package='',
  serialized_pb='\n\x0bLogin.proto\x1a\nUser.proto\x1a\x0eRuleList.proto\"]\n\x05Login\x12\x11\n\ttimestamp\x18\x01 \x01(\x05\x12\x18\n\x05rules\x18\x02 \x01(\x0b\x32\t.RuleList\x12\x13\n\x04user\x18\x03 \x01(\x0b\x32\x05.User\x12\x12\n\nfirst_time\x18\x04 \x01(\x08\x42&\n\x18\x63om.kloomba.app.protobufB\nLoginProto')




_LOGIN = descriptor.Descriptor(
  name='Login',
  full_name='Login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='timestamp', full_name='Login.timestamp', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rules', full_name='Login.rules', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user', full_name='Login.user', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='first_time', full_name='Login.first_time', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_end=136,
)

_LOGIN.fields_by_name['rules'].message_type = RuleList_pb2._RULELIST
_LOGIN.fields_by_name['user'].message_type = User_pb2._USER
DESCRIPTOR.message_types_by_name['Login'] = _LOGIN

class Login(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGIN
  
  # @@protoc_insertion_point(class_scope:Login)

# @@protoc_insertion_point(module_scope)