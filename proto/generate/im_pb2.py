# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: im.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='im.proto',
  package='im',
  syntax='proto3',
  serialized_pb=_b('\n\x08im.proto\x12\x02im\"\n\n\x08\x43_S_Ping\"\n\n\x08S_C_Ping\"&\n\tS_C_error\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x0b\n\x03msg\x18\x02 \x01(\t\"P\n\tC_S_infor\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x16\n\x0etarget_user_id\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61llback\x18\x04 \x01(\t\"^\n\tS_C_infor\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\r\n\x05other\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61llback\x18\x04 \x01(\t\x12\x15\n\rcallback_type\x18\x05 \x01(\t\"c\n\nmsgContent\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12\x11\n\timage_url\x18\x02 \x01(\t\x12\x10\n\x08\x66ile_url\x18\x03 \x01(\t\x12\x0c\n\x04time\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\t\"\x9b\x01\n\x0c\x43_S_Send_msg\x12\x0e\n\x06msg_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\x11\x12\x10\n\x08group_id\x18\x03 \x01(\x11\x12\x0c\n\x04type\x18\x04 \x01(\x07\x12\x15\n\rclient_msg_id\x18\x05 \x01(\t\x12\x12\n\nsession_id\x18\x06 \x01(\t\x12\x1f\n\x07Message\x18\x07 \x01(\x0b\x32\x0e.im.msgContent\"\xd9\x01\n\x0cS_C_Send_msg\x12\x0e\n\x06msg_id\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06sender\x18\x04 \x01(\x07\x12\x17\n\x0ftarget_group_id\x18\x05 \x01(\t\x12\x16\n\x0etarget_user_id\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x07 \x01(\x07\x12\x15\n\rclient_msg_id\x18\x08 \x01(\t\x12\r\n\x05state\x18\t \x01(\x07\x12\x1f\n\x07Message\x18\n \x01(\x0b\x32\x0e.im.msgContent\"V\n\rS_C_Send_Info\x12\x0e\n\x06msg_id\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\x11\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x15\n\rclient_msg_id\x18\x04 \x01(\t\"U\n\x0eofflineMessage\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x1e\n\x04info\x18\x03 \x03(\x0b\x32\x10.im.S_C_Send_msg\":\n\x13S_C_Offline_Message\x12#\n\x07offline\x18\x01 \x03(\x0b\x32\x12.im.offlineMessage\"\'\n\x06online\x12\x0f\n\x07user_id\x18\x01 \x01(\x11\x12\x0c\n\x04type\x18\x02 \x01(\x07\"(\n\nS_C_Online\x12\x1a\n\x06Online\x18\x01 \x03(\x0b\x32\n.im.online\"!\n\x0eS_C_Add_Online\x12\x0f\n\x07user_id\x18\x01 \x01(\x11\"\x1f\n\x0cS_C_Sign_Out\x12\x0f\n\x07user_id\x18\x01 \x01(\x11*\xa7\x02\n\tIM_HEADER\x12\x0b\n\x07\x46IRSTER\x10\x00\x12\x10\n\x08\x43_S_PING\x10\x81\x80\x80\x80\x01\x12\x10\n\x08S_C_PING\x10\x82\x80\x80\x80\x01\x12\x11\n\tS_C_ERROR\x10\x84\x88\x80\x82\x01\x12\x11\n\tC_S_INFOR\x10\x99\x83\x80\x81\x01\x12\x11\n\tS_C_INFOR\x10\x80\x84\x80\x81\x01\x12\x16\n\x10S_C_USER_LOGINED\x10\x82\x80@\x12\x10\n\x08\x43_S_SEND\x10\x81\x80\xc0\x80\x01\x12\x10\n\x08S_C_SEND\x10\x81\x80\x80\x81\x01\x12\x15\n\rS_C_SEND_INFO\x10\x82\x80\x80\x81\x01\x12\x12\n\nS_C_ONLINE\x10\x81\x82\x80\x81\x01\x12\x16\n\x0eS_C_ADD_ONLINE\x10\x82\x82\x80\x81\x01\x12\x14\n\x0cS_C_SIGN_OUT\x10\x83\x82\x80\x81\x01\x12\x1b\n\x13S_C_OFFLINE_MESSAGE\x10\x84\x82\x80\x81\x01\x62\x06proto3')
)

_IM_HEADER = _descriptor.EnumDescriptor(
  name='IM_HEADER',
  full_name='im.IM_HEADER',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FIRSTER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C_S_PING', index=1, number=268435457,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_PING', index=2, number=268435458,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_ERROR', index=3, number=272630788,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C_S_INFOR', index=4, number=270533017,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_INFOR', index=5, number=270533120,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_USER_LOGINED', index=6, number=1048578,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='C_S_SEND', index=7, number=269484033,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_SEND', index=8, number=270532609,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_SEND_INFO', index=9, number=270532610,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_ONLINE', index=10, number=270532865,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_ADD_ONLINE', index=11, number=270532866,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_SIGN_OUT', index=12, number=270532867,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='S_C_OFFLINE_MESSAGE', index=13, number=270532868,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1124,
  serialized_end=1419,
)
_sym_db.RegisterEnumDescriptor(_IM_HEADER)

IM_HEADER = enum_type_wrapper.EnumTypeWrapper(_IM_HEADER)
FIRSTER = 0
C_S_PING = 268435457
S_C_PING = 268435458
S_C_ERROR = 272630788
C_S_INFOR = 270533017
S_C_INFOR = 270533120
S_C_USER_LOGINED = 1048578
C_S_SEND = 269484033
S_C_SEND = 270532609
S_C_SEND_INFO = 270532610
S_C_ONLINE = 270532865
S_C_ADD_ONLINE = 270532866
S_C_SIGN_OUT = 270532867
S_C_OFFLINE_MESSAGE = 270532868



_C_S_PING = _descriptor.Descriptor(
  name='C_S_Ping',
  full_name='im.C_S_Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=26,
)


_S_C_PING = _descriptor.Descriptor(
  name='S_C_Ping',
  full_name='im.S_C_Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=38,
)


_S_C_ERROR = _descriptor.Descriptor(
  name='S_C_error',
  full_name='im.S_C_error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='im.S_C_error.code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='im.S_C_error.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=78,
)


_C_S_INFOR = _descriptor.Descriptor(
  name='C_S_infor',
  full_name='im.C_S_infor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='im.C_S_infor.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='im.C_S_infor.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_user_id', full_name='im.C_S_infor.target_user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback', full_name='im.C_S_infor.callback', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=160,
)


_S_C_INFOR = _descriptor.Descriptor(
  name='S_C_infor',
  full_name='im.S_C_infor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='im.S_C_infor.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='im.S_C_infor.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other', full_name='im.S_C_infor.other', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback', full_name='im.S_C_infor.callback', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback_type', full_name='im.S_C_infor.callback_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=256,
)


_MSGCONTENT = _descriptor.Descriptor(
  name='msgContent',
  full_name='im.msgContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='im.msgContent.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='im.msgContent.image_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_url', full_name='im.msgContent.file_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='im.msgContent.time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='im.msgContent.timestamp', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=357,
)


_C_S_SEND_MSG = _descriptor.Descriptor(
  name='C_S_Send_msg',
  full_name='im.C_S_Send_msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='im.C_S_Send_msg.msg_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='im.C_S_Send_msg.user_id', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='im.C_S_Send_msg.group_id', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='im.C_S_Send_msg.type', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_msg_id', full_name='im.C_S_Send_msg.client_msg_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='im.C_S_Send_msg.session_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Message', full_name='im.C_S_Send_msg.Message', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=360,
  serialized_end=515,
)


_S_C_SEND_MSG = _descriptor.Descriptor(
  name='S_C_Send_msg',
  full_name='im.S_C_Send_msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='im.S_C_Send_msg.msg_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='im.S_C_Send_msg.session_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='im.S_C_Send_msg.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender', full_name='im.S_C_Send_msg.sender', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_group_id', full_name='im.S_C_Send_msg.target_group_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_user_id', full_name='im.S_C_Send_msg.target_user_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='im.S_C_Send_msg.type', index=6,
      number=7, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_msg_id', full_name='im.S_C_Send_msg.client_msg_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='im.S_C_Send_msg.state', index=8,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Message', full_name='im.S_C_Send_msg.Message', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=518,
  serialized_end=735,
)


_S_C_SEND_INFO = _descriptor.Descriptor(
  name='S_C_Send_Info',
  full_name='im.S_C_Send_Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='im.S_C_Send_Info.msg_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='im.S_C_Send_Info.state', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='im.S_C_Send_Info.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_msg_id', full_name='im.S_C_Send_Info.client_msg_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=737,
  serialized_end=823,
)


_OFFLINEMESSAGE = _descriptor.Descriptor(
  name='offlineMessage',
  full_name='im.offlineMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='im.offlineMessage.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='im.offlineMessage.session_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='im.offlineMessage.info', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=825,
  serialized_end=910,
)


_S_C_OFFLINE_MESSAGE = _descriptor.Descriptor(
  name='S_C_Offline_Message',
  full_name='im.S_C_Offline_Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offline', full_name='im.S_C_Offline_Message.offline', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=912,
  serialized_end=970,
)


_ONLINE = _descriptor.Descriptor(
  name='online',
  full_name='im.online',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='im.online.user_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='im.online.type', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=972,
  serialized_end=1011,
)


_S_C_ONLINE = _descriptor.Descriptor(
  name='S_C_Online',
  full_name='im.S_C_Online',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Online', full_name='im.S_C_Online.Online', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1013,
  serialized_end=1053,
)


_S_C_ADD_ONLINE = _descriptor.Descriptor(
  name='S_C_Add_Online',
  full_name='im.S_C_Add_Online',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='im.S_C_Add_Online.user_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1055,
  serialized_end=1088,
)


_S_C_SIGN_OUT = _descriptor.Descriptor(
  name='S_C_Sign_Out',
  full_name='im.S_C_Sign_Out',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='im.S_C_Sign_Out.user_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1090,
  serialized_end=1121,
)

_C_S_SEND_MSG.fields_by_name['Message'].message_type = _MSGCONTENT
_S_C_SEND_MSG.fields_by_name['Message'].message_type = _MSGCONTENT
_OFFLINEMESSAGE.fields_by_name['info'].message_type = _S_C_SEND_MSG
_S_C_OFFLINE_MESSAGE.fields_by_name['offline'].message_type = _OFFLINEMESSAGE
_S_C_ONLINE.fields_by_name['Online'].message_type = _ONLINE
DESCRIPTOR.message_types_by_name['C_S_Ping'] = _C_S_PING
DESCRIPTOR.message_types_by_name['S_C_Ping'] = _S_C_PING
DESCRIPTOR.message_types_by_name['S_C_error'] = _S_C_ERROR
DESCRIPTOR.message_types_by_name['C_S_infor'] = _C_S_INFOR
DESCRIPTOR.message_types_by_name['S_C_infor'] = _S_C_INFOR
DESCRIPTOR.message_types_by_name['msgContent'] = _MSGCONTENT
DESCRIPTOR.message_types_by_name['C_S_Send_msg'] = _C_S_SEND_MSG
DESCRIPTOR.message_types_by_name['S_C_Send_msg'] = _S_C_SEND_MSG
DESCRIPTOR.message_types_by_name['S_C_Send_Info'] = _S_C_SEND_INFO
DESCRIPTOR.message_types_by_name['offlineMessage'] = _OFFLINEMESSAGE
DESCRIPTOR.message_types_by_name['S_C_Offline_Message'] = _S_C_OFFLINE_MESSAGE
DESCRIPTOR.message_types_by_name['online'] = _ONLINE
DESCRIPTOR.message_types_by_name['S_C_Online'] = _S_C_ONLINE
DESCRIPTOR.message_types_by_name['S_C_Add_Online'] = _S_C_ADD_ONLINE
DESCRIPTOR.message_types_by_name['S_C_Sign_Out'] = _S_C_SIGN_OUT
DESCRIPTOR.enum_types_by_name['IM_HEADER'] = _IM_HEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C_S_Ping = _reflection.GeneratedProtocolMessageType('C_S_Ping', (_message.Message,), dict(
  DESCRIPTOR = _C_S_PING,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.C_S_Ping)
  ))
_sym_db.RegisterMessage(C_S_Ping)

S_C_Ping = _reflection.GeneratedProtocolMessageType('S_C_Ping', (_message.Message,), dict(
  DESCRIPTOR = _S_C_PING,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.S_C_Ping)
  ))
_sym_db.RegisterMessage(S_C_Ping)

S_C_error = _reflection.GeneratedProtocolMessageType('S_C_error', (_message.Message,), dict(
  DESCRIPTOR = _S_C_ERROR,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.S_C_error)
  ))
_sym_db.RegisterMessage(S_C_error)

C_S_infor = _reflection.GeneratedProtocolMessageType('C_S_infor', (_message.Message,), dict(
  DESCRIPTOR = _C_S_INFOR,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.C_S_infor)
  ))
_sym_db.RegisterMessage(C_S_infor)

S_C_infor = _reflection.GeneratedProtocolMessageType('S_C_infor', (_message.Message,), dict(
  DESCRIPTOR = _S_C_INFOR,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.S_C_infor)
  ))
_sym_db.RegisterMessage(S_C_infor)

msgContent = _reflection.GeneratedProtocolMessageType('msgContent', (_message.Message,), dict(
  DESCRIPTOR = _MSGCONTENT,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.msgContent)
  ))
_sym_db.RegisterMessage(msgContent)

C_S_Send_msg = _reflection.GeneratedProtocolMessageType('C_S_Send_msg', (_message.Message,), dict(
  DESCRIPTOR = _C_S_SEND_MSG,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.C_S_Send_msg)
  ))
_sym_db.RegisterMessage(C_S_Send_msg)

S_C_Send_msg = _reflection.GeneratedProtocolMessageType('S_C_Send_msg', (_message.Message,), dict(
  DESCRIPTOR = _S_C_SEND_MSG,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.S_C_Send_msg)
  ))
_sym_db.RegisterMessage(S_C_Send_msg)

S_C_Send_Info = _reflection.GeneratedProtocolMessageType('S_C_Send_Info', (_message.Message,), dict(
  DESCRIPTOR = _S_C_SEND_INFO,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.S_C_Send_Info)
  ))
_sym_db.RegisterMessage(S_C_Send_Info)

offlineMessage = _reflection.GeneratedProtocolMessageType('offlineMessage', (_message.Message,), dict(
  DESCRIPTOR = _OFFLINEMESSAGE,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.offlineMessage)
  ))
_sym_db.RegisterMessage(offlineMessage)

S_C_Offline_Message = _reflection.GeneratedProtocolMessageType('S_C_Offline_Message', (_message.Message,), dict(
  DESCRIPTOR = _S_C_OFFLINE_MESSAGE,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.S_C_Offline_Message)
  ))
_sym_db.RegisterMessage(S_C_Offline_Message)

online = _reflection.GeneratedProtocolMessageType('online', (_message.Message,), dict(
  DESCRIPTOR = _ONLINE,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.online)
  ))
_sym_db.RegisterMessage(online)

S_C_Online = _reflection.GeneratedProtocolMessageType('S_C_Online', (_message.Message,), dict(
  DESCRIPTOR = _S_C_ONLINE,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.S_C_Online)
  ))
_sym_db.RegisterMessage(S_C_Online)

S_C_Add_Online = _reflection.GeneratedProtocolMessageType('S_C_Add_Online', (_message.Message,), dict(
  DESCRIPTOR = _S_C_ADD_ONLINE,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.S_C_Add_Online)
  ))
_sym_db.RegisterMessage(S_C_Add_Online)

S_C_Sign_Out = _reflection.GeneratedProtocolMessageType('S_C_Sign_Out', (_message.Message,), dict(
  DESCRIPTOR = _S_C_SIGN_OUT,
  __module__ = 'im_pb2'
  # @@protoc_insertion_point(class_scope:im.S_C_Sign_Out)
  ))
_sym_db.RegisterMessage(S_C_Sign_Out)


# @@protoc_insertion_point(module_scope)
