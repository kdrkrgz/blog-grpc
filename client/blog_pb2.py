# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blog.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nblog.proto\"\x19\n\x0bPostRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"7\n\x0cPostResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\"\x11\n\x0fListPostRequest\"0\n\x10ListPostResponse\x12\x1c\n\x05posts\x18\x01 \x03(\x0b\x32\r.PostResponse2i\n\x0b\x42logService\x12(\n\tQueryPost\x12\x0c.PostRequest\x1a\r.PostResponse\x12\x30\n\tListPosts\x12\x10.ListPostRequest\x1a\x11.ListPostResponseB\x0eZ\x0cserver/blog/b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'blog_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\014server/blog/'
  _POSTREQUEST._serialized_start=14
  _POSTREQUEST._serialized_end=39
  _POSTRESPONSE._serialized_start=41
  _POSTRESPONSE._serialized_end=96
  _LISTPOSTREQUEST._serialized_start=98
  _LISTPOSTREQUEST._serialized_end=115
  _LISTPOSTRESPONSE._serialized_start=117
  _LISTPOSTRESPONSE._serialized_end=165
  _BLOGSERVICE._serialized_start=167
  _BLOGSERVICE._serialized_end=272
# @@protoc_insertion_point(module_scope)