# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filesw.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='filesw.proto',
  package='file',
  syntax='proto3',
  serialized_options=b'\n\025io.grpc.examples.fileB\tFileProtoP\001\242\002\003fsw',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x66ilesw.proto\x12\x04\x66ile\"%\n\x05\x43PReq\x12\r\n\x05\x66ile1\x18\x01 \x01(\t\x12\r\n\x05\x66ile2\x18\x02 \x01(\t\"\x17\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x18\n\x08Response\x12\x0c\n\x04name\x18\x01 \x01(\t\":\n\x05\x46iles\x12\x1e\n\x04\x66ile\x18\x01 \x03(\x0b\x32\x10.file.Files.name\x1a\x11\n\x04name\x12\t\n\x01n\x18\x01 \x01(\t2\xfd\x01\n\nFileServer\x12%\n\x02LS\x12\r.file.Request\x1a\x0e.file.Response\"\x00\x12&\n\x03\x43\x41T\x12\r.file.Request\x1a\x0e.file.Response\"\x00\x12%\n\x02\x43P\x12\r.file.Request\x1a\x0e.file.Response\"\x00\x12&\n\x03PWD\x12\r.file.Request\x1a\x0e.file.Response\"\x00\x12&\n\x03NEW\x12\r.file.Request\x1a\x0e.file.Response\"\x00\x12)\n\x08ShareKey\x12\x0b.file.CPReq\x1a\x0e.file.Response\"\x00\x42*\n\x15io.grpc.examples.fileB\tFileProtoP\x01\xa2\x02\x03\x66swb\x06proto3'
)




_CPREQ = _descriptor.Descriptor(
  name='CPReq',
  full_name='file.CPReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file1', full_name='file.CPReq.file1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file2', full_name='file.CPReq.file2', index=1,
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
  serialized_start=22,
  serialized_end=59,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='file.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='file.Request.name', index=0,
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
  serialized_start=61,
  serialized_end=84,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='file.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='file.Response.name', index=0,
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
  serialized_start=86,
  serialized_end=110,
)


_FILES_NAME = _descriptor.Descriptor(
  name='name',
  full_name='file.Files.name',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='n', full_name='file.Files.name.n', index=0,
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
  serialized_start=153,
  serialized_end=170,
)

_FILES = _descriptor.Descriptor(
  name='Files',
  full_name='file.Files',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='file.Files.file', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FILES_NAME, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=170,
)

_FILES_NAME.containing_type = _FILES
_FILES.fields_by_name['file'].message_type = _FILES_NAME
DESCRIPTOR.message_types_by_name['CPReq'] = _CPREQ
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Files'] = _FILES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CPReq = _reflection.GeneratedProtocolMessageType('CPReq', (_message.Message,), {
  'DESCRIPTOR' : _CPREQ,
  '__module__' : 'filesw_pb2'
  # @@protoc_insertion_point(class_scope:file.CPReq)
  })
_sym_db.RegisterMessage(CPReq)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'filesw_pb2'
  # @@protoc_insertion_point(class_scope:file.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'filesw_pb2'
  # @@protoc_insertion_point(class_scope:file.Response)
  })
_sym_db.RegisterMessage(Response)

Files = _reflection.GeneratedProtocolMessageType('Files', (_message.Message,), {

  'name' : _reflection.GeneratedProtocolMessageType('name', (_message.Message,), {
    'DESCRIPTOR' : _FILES_NAME,
    '__module__' : 'filesw_pb2'
    # @@protoc_insertion_point(class_scope:file.Files.name)
    })
  ,
  'DESCRIPTOR' : _FILES,
  '__module__' : 'filesw_pb2'
  # @@protoc_insertion_point(class_scope:file.Files)
  })
_sym_db.RegisterMessage(Files)
_sym_db.RegisterMessage(Files.name)


DESCRIPTOR._options = None

_FILESERVER = _descriptor.ServiceDescriptor(
  name='FileServer',
  full_name='file.FileServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=173,
  serialized_end=426,
  methods=[
  _descriptor.MethodDescriptor(
    name='LS',
    full_name='file.FileServer.LS',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CAT',
    full_name='file.FileServer.CAT',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CP',
    full_name='file.FileServer.CP',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PWD',
    full_name='file.FileServer.PWD',
    index=3,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='NEW',
    full_name='file.FileServer.NEW',
    index=4,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ShareKey',
    full_name='file.FileServer.ShareKey',
    index=5,
    containing_service=None,
    input_type=_CPREQ,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILESERVER)

DESCRIPTOR.services_by_name['FileServer'] = _FILESERVER

# @@protoc_insertion_point(module_scope)
