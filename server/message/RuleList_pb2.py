# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.net.proto2.python.public import descriptor
from google.net.proto2.python.public import message
from google.net.proto2.python.public import reflection
from google.net.proto2.proto import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='RuleList.proto',
  package='',
  serialized_pb='\n\x0eRuleList.proto\"\'\n\x08RuleItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"6\n\x08RuleList\x12\x11\n\ttimestamp\x18\x01 \x01(\x05\x12\x17\n\x04item\x18\x02 \x03(\x0b\x32\t.RuleItemB&\n\x15\x63om.kloomba.rule.listB\rRuleListProto')




_RULEITEM = descriptor.Descriptor(
  name='RuleItem',
  full_name='RuleItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='RuleItem.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='RuleItem.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=18,
  serialized_end=57,
)


_RULELIST = descriptor.Descriptor(
  name='RuleList',
  full_name='RuleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='timestamp', full_name='RuleList.timestamp', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item', full_name='RuleList.item', index=1,
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
  serialized_start=59,
  serialized_end=113,
)

_RULELIST.fields_by_name['item'].message_type = _RULEITEM
DESCRIPTOR.message_types_by_name['RuleItem'] = _RULEITEM
DESCRIPTOR.message_types_by_name['RuleList'] = _RULELIST

class RuleItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RULEITEM
  
  # @@protoc_insertion_point(class_scope:RuleItem)

class RuleList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RULELIST
  
  # @@protoc_insertion_point(class_scope:RuleList)

# @@protoc_insertion_point(module_scope)
