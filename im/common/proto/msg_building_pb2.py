# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_building.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_building.proto',
  package='msg_building',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12msg_building.proto\x12\x0cmsg_building\"@\n\x10\x62uild_conditions\x12\x0c\n\x04type\x18\x01 \x01(\x07\x12\r\n\x05value\x18\x02 \x01(\x07\x12\x0f\n\x07reasion\x18\x03 \x01(\t\"X\n\x0e\x62uild_attribut\x12\x0c\n\x04type\x18\x01 \x01(\x07\x12\x15\n\rgenerate_time\x18\x02 \x01(\x07\x12\x0e\n\x06repeat\x18\x03 \x01(\x11\x12\x11\n\tresult_id\x18\x04 \x01(\x07\"\xcd\x01\n\rbuild_details\x12\n\n\x02id\x18\x01 \x01(\x07\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\t\x12\x11\n\tparent_id\x18\x04 \x01(\x07\x12\x32\n\nconditions\x18\x05 \x03(\x0b\x32\x1e.msg_building.build_conditions\x12\x1b\n\x13\x62uild_generate_type\x18\x06 \x01(\x07\x12/\n\tattribute\x18\x07 \x03(\x0b\x32\x1c.msg_building.build_attribut\";\n\rbuilding_list\x12*\n\x05\x62uild\x18\x01 \x03(\x0b\x32\x1b.msg_building.build_detailsb\x06proto3')
)




_BUILD_CONDITIONS = _descriptor.Descriptor(
  name='build_conditions',
  full_name='msg_building.build_conditions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='msg_building.build_conditions.type', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='msg_building.build_conditions.value', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reasion', full_name='msg_building.build_conditions.reasion', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=36,
  serialized_end=100,
)


_BUILD_ATTRIBUT = _descriptor.Descriptor(
  name='build_attribut',
  full_name='msg_building.build_attribut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='msg_building.build_attribut.type', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generate_time', full_name='msg_building.build_attribut.generate_time', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeat', full_name='msg_building.build_attribut.repeat', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_id', full_name='msg_building.build_attribut.result_id', index=3,
      number=4, type=7, cpp_type=3, label=1,
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
  serialized_start=102,
  serialized_end=190,
)


_BUILD_DETAILS = _descriptor.Descriptor(
  name='build_details',
  full_name='msg_building.build_details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='msg_building.build_details.id', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='msg_building.build_details.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='msg_building.build_details.level', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='msg_building.build_details.parent_id', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conditions', full_name='msg_building.build_details.conditions', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_generate_type', full_name='msg_building.build_details.build_generate_type', index=5,
      number=6, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='msg_building.build_details.attribute', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  serialized_start=193,
  serialized_end=398,
)


_BUILDING_LIST = _descriptor.Descriptor(
  name='building_list',
  full_name='msg_building.building_list',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build', full_name='msg_building.building_list.build', index=0,
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
  serialized_start=400,
  serialized_end=459,
)

_BUILD_DETAILS.fields_by_name['conditions'].message_type = _BUILD_CONDITIONS
_BUILD_DETAILS.fields_by_name['attribute'].message_type = _BUILD_ATTRIBUT
_BUILDING_LIST.fields_by_name['build'].message_type = _BUILD_DETAILS
DESCRIPTOR.message_types_by_name['build_conditions'] = _BUILD_CONDITIONS
DESCRIPTOR.message_types_by_name['build_attribut'] = _BUILD_ATTRIBUT
DESCRIPTOR.message_types_by_name['build_details'] = _BUILD_DETAILS
DESCRIPTOR.message_types_by_name['building_list'] = _BUILDING_LIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

build_conditions = _reflection.GeneratedProtocolMessageType('build_conditions', (_message.Message,), dict(
  DESCRIPTOR = _BUILD_CONDITIONS,
  __module__ = 'msg_building_pb2'
  # @@protoc_insertion_point(class_scope:msg_building.build_conditions)
  ))
_sym_db.RegisterMessage(build_conditions)

build_attribut = _reflection.GeneratedProtocolMessageType('build_attribut', (_message.Message,), dict(
  DESCRIPTOR = _BUILD_ATTRIBUT,
  __module__ = 'msg_building_pb2'
  # @@protoc_insertion_point(class_scope:msg_building.build_attribut)
  ))
_sym_db.RegisterMessage(build_attribut)

build_details = _reflection.GeneratedProtocolMessageType('build_details', (_message.Message,), dict(
  DESCRIPTOR = _BUILD_DETAILS,
  __module__ = 'msg_building_pb2'
  # @@protoc_insertion_point(class_scope:msg_building.build_details)
  ))
_sym_db.RegisterMessage(build_details)

building_list = _reflection.GeneratedProtocolMessageType('building_list', (_message.Message,), dict(
  DESCRIPTOR = _BUILDING_LIST,
  __module__ = 'msg_building_pb2'
  # @@protoc_insertion_point(class_scope:msg_building.building_list)
  ))
_sym_db.RegisterMessage(building_list)


# @@protoc_insertion_point(module_scope)
