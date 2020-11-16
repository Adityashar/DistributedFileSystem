# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: central.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='central.proto',
  package='central',
  syntax='proto3',
  serialized_options=b'\n\030io.grpc.examples.centralB\014CentralProtoP\001\242\002\003CNT',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rcentral.proto\x12\x07\x63\x65ntral\"\x17\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x19\n\tResponse2\x12\x0c\n\x04name\x18\x01 \x01(\t\"[\n\x08Response\x12\"\n\x04serv\x18\x01 \x03(\x0b\x32\x14.central.Response.Fs\x12\x0b\n\x03num\x18\x02 \x01(\x05\x1a\x1e\n\x02\x46s\x12\x0c\n\x04port\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t2\xa5\x01\n\x07\x43\x65ntral\x12\x30\n\x06GiveFS\x12\x10.central.Request\x1a\x12.central.Response2\"\x00\x12\x36\n\x0cRegistration\x12\x10.central.Request\x1a\x12.central.Response2\"\x00\x12\x30\n\x06GenKey\x12\x10.central.Request\x1a\x12.central.Response2\"\x00\x42\x30\n\x18io.grpc.examples.centralB\x0c\x43\x65ntralProtoP\x01\xa2\x02\x03\x43NTb\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='central.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='central.Request.name', index=0,
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
  serialized_start=26,
  serialized_end=49,
)


_RESPONSE2 = _descriptor.Descriptor(
  name='Response2',
  full_name='central.Response2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='central.Response2.name', index=0,
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
  serialized_start=51,
  serialized_end=76,
)


_RESPONSE_FS = _descriptor.Descriptor(
  name='Fs',
  full_name='central.Response.Fs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='central.Response.Fs.port', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='central.Response.Fs.id', index=1,
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
  serialized_start=139,
  serialized_end=169,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='central.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serv', full_name='central.Response.serv', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num', full_name='central.Response.num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_FS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=169,
)

_RESPONSE_FS.containing_type = _RESPONSE
_RESPONSE.fields_by_name['serv'].message_type = _RESPONSE_FS
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response2'] = _RESPONSE2
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'central_pb2'
  # @@protoc_insertion_point(class_scope:central.Request)
  })
_sym_db.RegisterMessage(Request)

Response2 = _reflection.GeneratedProtocolMessageType('Response2', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE2,
  '__module__' : 'central_pb2'
  # @@protoc_insertion_point(class_scope:central.Response2)
  })
_sym_db.RegisterMessage(Response2)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {

  'Fs' : _reflection.GeneratedProtocolMessageType('Fs', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSE_FS,
    '__module__' : 'central_pb2'
    # @@protoc_insertion_point(class_scope:central.Response.Fs)
    })
  ,
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'central_pb2'
  # @@protoc_insertion_point(class_scope:central.Response)
  })
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Fs)


DESCRIPTOR._options = None

_CENTRAL = _descriptor.ServiceDescriptor(
  name='Central',
  full_name='central.Central',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=172,
  serialized_end=337,
  methods=[
  _descriptor.MethodDescriptor(
    name='GiveFS',
    full_name='central.Central.GiveFS',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE2,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Registration',
    full_name='central.Central.Registration',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE2,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GenKey',
    full_name='central.Central.GenKey',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE2,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CENTRAL)

DESCRIPTOR.services_by_name['Central'] = _CENTRAL

# @@protoc_insertion_point(module_scope)
