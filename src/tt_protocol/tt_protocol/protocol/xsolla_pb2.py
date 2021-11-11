# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xsolla.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xsolla.proto',
  package='xsolla',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cxsolla.proto\x12\x06xsolla\"J\n\x0b\x41\x63\x63ountInfo\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x12\n\nreturn_url\x18\x04 \x01(\t\"J\n\x0fGetTokenRequest\x12)\n\x0c\x61\x63\x63ount_info\x18\x01 \x01(\x0b\x32\x13.xsolla.AccountInfo\x12\x0c\n\x04mode\x18\x02 \x01(\t\"!\n\x10GetTokenResponse\x12\r\n\x05token\x18\x01 \x01(\t\"I\n\x13PaymentCallbackBody\x12\x12\n\naccount_id\x18\x01 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\x12\x0e\n\x06secret\x18\x03 \x01(\t\"\x17\n\x15PaymentCallbackAnswer\"\x1a\n\x18\x44\x65\x62ugClearServiceRequest\"\x1b\n\x19\x44\x65\x62ugClearServiceResponseb\x06proto3'
)




_ACCOUNTINFO = _descriptor.Descriptor(
  name='AccountInfo',
  full_name='xsolla.AccountInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='xsolla.AccountInfo.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='xsolla.AccountInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='xsolla.AccountInfo.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='return_url', full_name='xsolla.AccountInfo.return_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=24,
  serialized_end=98,
)


_GETTOKENREQUEST = _descriptor.Descriptor(
  name='GetTokenRequest',
  full_name='xsolla.GetTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_info', full_name='xsolla.GetTokenRequest.account_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='xsolla.GetTokenRequest.mode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=100,
  serialized_end=174,
)


_GETTOKENRESPONSE = _descriptor.Descriptor(
  name='GetTokenResponse',
  full_name='xsolla.GetTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='xsolla.GetTokenResponse.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=176,
  serialized_end=209,
)


_PAYMENTCALLBACKBODY = _descriptor.Descriptor(
  name='PaymentCallbackBody',
  full_name='xsolla.PaymentCallbackBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='xsolla.PaymentCallbackBody.account_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='xsolla.PaymentCallbackBody.amount', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret', full_name='xsolla.PaymentCallbackBody.secret', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=211,
  serialized_end=284,
)


_PAYMENTCALLBACKANSWER = _descriptor.Descriptor(
  name='PaymentCallbackAnswer',
  full_name='xsolla.PaymentCallbackAnswer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=286,
  serialized_end=309,
)


_DEBUGCLEARSERVICEREQUEST = _descriptor.Descriptor(
  name='DebugClearServiceRequest',
  full_name='xsolla.DebugClearServiceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=311,
  serialized_end=337,
)


_DEBUGCLEARSERVICERESPONSE = _descriptor.Descriptor(
  name='DebugClearServiceResponse',
  full_name='xsolla.DebugClearServiceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=339,
  serialized_end=366,
)

_GETTOKENREQUEST.fields_by_name['account_info'].message_type = _ACCOUNTINFO
DESCRIPTOR.message_types_by_name['AccountInfo'] = _ACCOUNTINFO
DESCRIPTOR.message_types_by_name['GetTokenRequest'] = _GETTOKENREQUEST
DESCRIPTOR.message_types_by_name['GetTokenResponse'] = _GETTOKENRESPONSE
DESCRIPTOR.message_types_by_name['PaymentCallbackBody'] = _PAYMENTCALLBACKBODY
DESCRIPTOR.message_types_by_name['PaymentCallbackAnswer'] = _PAYMENTCALLBACKANSWER
DESCRIPTOR.message_types_by_name['DebugClearServiceRequest'] = _DEBUGCLEARSERVICEREQUEST
DESCRIPTOR.message_types_by_name['DebugClearServiceResponse'] = _DEBUGCLEARSERVICERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountInfo = _reflection.GeneratedProtocolMessageType('AccountInfo', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTINFO,
  '__module__' : 'xsolla_pb2'
  # @@protoc_insertion_point(class_scope:xsolla.AccountInfo)
  })
_sym_db.RegisterMessage(AccountInfo)

GetTokenRequest = _reflection.GeneratedProtocolMessageType('GetTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTOKENREQUEST,
  '__module__' : 'xsolla_pb2'
  # @@protoc_insertion_point(class_scope:xsolla.GetTokenRequest)
  })
_sym_db.RegisterMessage(GetTokenRequest)

GetTokenResponse = _reflection.GeneratedProtocolMessageType('GetTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTOKENRESPONSE,
  '__module__' : 'xsolla_pb2'
  # @@protoc_insertion_point(class_scope:xsolla.GetTokenResponse)
  })
_sym_db.RegisterMessage(GetTokenResponse)

PaymentCallbackBody = _reflection.GeneratedProtocolMessageType('PaymentCallbackBody', (_message.Message,), {
  'DESCRIPTOR' : _PAYMENTCALLBACKBODY,
  '__module__' : 'xsolla_pb2'
  # @@protoc_insertion_point(class_scope:xsolla.PaymentCallbackBody)
  })
_sym_db.RegisterMessage(PaymentCallbackBody)

PaymentCallbackAnswer = _reflection.GeneratedProtocolMessageType('PaymentCallbackAnswer', (_message.Message,), {
  'DESCRIPTOR' : _PAYMENTCALLBACKANSWER,
  '__module__' : 'xsolla_pb2'
  # @@protoc_insertion_point(class_scope:xsolla.PaymentCallbackAnswer)
  })
_sym_db.RegisterMessage(PaymentCallbackAnswer)

DebugClearServiceRequest = _reflection.GeneratedProtocolMessageType('DebugClearServiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGCLEARSERVICEREQUEST,
  '__module__' : 'xsolla_pb2'
  # @@protoc_insertion_point(class_scope:xsolla.DebugClearServiceRequest)
  })
_sym_db.RegisterMessage(DebugClearServiceRequest)

DebugClearServiceResponse = _reflection.GeneratedProtocolMessageType('DebugClearServiceResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGCLEARSERVICERESPONSE,
  '__module__' : 'xsolla_pb2'
  # @@protoc_insertion_point(class_scope:xsolla.DebugClearServiceResponse)
  })
_sym_db.RegisterMessage(DebugClearServiceResponse)


# @@protoc_insertion_point(module_scope)
