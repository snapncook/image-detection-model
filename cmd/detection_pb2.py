# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: detection.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'detection.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x64\x65tection.proto\x12\x0f\x64\x65tection_proto\",\n\x14YOLODetectionRequest\x12\x14\n\x05image\x18\x01 \x01(\x0cR\x05image\"1\n\x15YOLODetectionResponse\x12\x18\n\x07objects\x18\x01 \x03(\tR\x07objects2q\n\x10\x44\x65tectionService\x12]\n\nYOLODetect\x12%.detection_proto.YOLODetectionRequest\x1a&.detection_proto.YOLODetectionResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'detection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_YOLODETECTIONREQUEST']._serialized_start=36
  _globals['_YOLODETECTIONREQUEST']._serialized_end=80
  _globals['_YOLODETECTIONRESPONSE']._serialized_start=82
  _globals['_YOLODETECTIONRESPONSE']._serialized_end=131
  _globals['_DETECTIONSERVICE']._serialized_start=133
  _globals['_DETECTIONSERVICE']._serialized_end=246
# @@protoc_insertion_point(module_scope)
