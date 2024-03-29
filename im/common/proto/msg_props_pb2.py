# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_props.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_props.proto',
  package='msg_props',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fmsg_props.proto\x12\tmsg_props\"z\n\x0fprops_attribute\x12\x0c\n\x04type\x18\x01 \x01(\x07\x12\r\n\x05value\x18\x02 \x01(\t\x12\x10\n\x08use_type\x18\x03 \x01(\x07\x12\x18\n\x10time_of_duration\x18\x04 \x01(\x07\x12\x1e\n\x16start_time_of_duration\x18\x05 \x01(\x07\"f\n\rprops_details\x12\n\n\x02id\x18\x01 \x01(\x07\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\x07\x12-\n\tattribute\x18\x05 \x03(\x0b\x32\x1a.msg_props.props_attribute\"7\n\nprops_List\x12)\n\x07\x64\x65tails\x18\x01 \x03(\x0b\x32\x18.msg_props.props_detailsb\x06proto3')
)




_PROPS_ATTRIBUTE = _descriptor.Descriptor(
  name='props_attribute',
  full_name='msg_props.props_attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='msg_props.props_attribute.type', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='msg_props.props_attribute.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_type', full_name='msg_props.props_attribute.use_type', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_of_duration', full_name='msg_props.props_attribute.time_of_duration', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time_of_duration', full_name='msg_props.props_attribute.start_time_of_duration', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=152,
)


_PROPS_DETAILS = _descriptor.Descriptor(
  name='props_details',
  full_name='msg_props.props_details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='msg_props.props_details.id', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='msg_props.props_details.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='msg_props.props_details.type', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='msg_props.props_details.attribute', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=256,
)


_PROPS_LIST = _descriptor.Descriptor(
  name='props_List',
  full_name='msg_props.props_List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='msg_props.props_List.details', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=313,
)

_PROPS_DETAILS.fields_by_name['attribute'].message_type = _PROPS_ATTRIBUTE
_PROPS_LIST.fields_by_name['details'].message_type = _PROPS_DETAILS
DESCRIPTOR.message_types_by_name['props_attribute'] = _PROPS_ATTRIBUTE
DESCRIPTOR.message_types_by_name['props_details'] = _PROPS_DETAILS
DESCRIPTOR.message_types_by_name['props_List'] = _PROPS_LIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

props_attribute = _reflection.GeneratedProtocolMessageType('props_attribute', (_message.Message,), dict(
  DESCRIPTOR = _PROPS_ATTRIBUTE,
  __module__ = 'msg_props_pb2'
  # @@protoc_insertion_point(class_scope:msg_props.props_attribute)
  ))
_sym_db.RegisterMessage(props_attribute)

props_details = _reflection.GeneratedProtocolMessageType('props_details', (_message.Message,), dict(
  DESCRIPTOR = _PROPS_DETAILS,
  __module__ = 'msg_props_pb2'
  # @@protoc_insertion_point(class_scope:msg_props.props_details)
  ))
_sym_db.RegisterMessage(props_details)

props_List = _reflection.GeneratedProtocolMessageType('props_List', (_message.Message,), dict(
  DESCRIPTOR = _PROPS_LIST,
  __module__ = 'msg_props_pb2'
  # @@protoc_insertion_point(class_scope:msg_props.props_List)
  ))
_sym_db.RegisterMessage(props_List)


# @@protoc_insertion_point(module_scope)
