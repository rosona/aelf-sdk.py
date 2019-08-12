# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='types.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0btypes.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\"\n\x0bStringInput\x12\x13\n\x0bStringValue\x18\x01 \x01(\t\" \n\tMinerList\x12\x13\n\x0bpublic_keys\x18\x01 \x03(\x0c\"\x15\n\x04Hash\x12\r\n\x05Value\x18\x01 \x01(\x0c\"\x18\n\x07\x41\x64\x64ress\x12\r\n\x05Value\x18\x01 \x01(\x0c\"\xa3\x01\n\x0bTransaction\x12\x16\n\x04\x46rom\x18\x01 \x01(\x0b\x32\x08.Address\x12\x14\n\x02To\x18\x02 \x01(\x0b\x32\x08.Address\x12\x16\n\x0eRefBlockNumber\x18\x03 \x01(\x03\x12\x16\n\x0eRefBlockPrefix\x18\x04 \x01(\x0c\x12\x12\n\nMethodName\x18\x05 \x01(\t\x12\x0e\n\x06Params\x18\x06 \x01(\x0c\x12\x12\n\tSignature\x18\x90N \x01(\x0c\"\xca\x02\n\x14\x45lectionVotingRecord\x12\x17\n\x05voter\x18\x01 \x01(\x0b\x32\x08.Address\x12\x11\n\tcandidate\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x12\x12\x13\n\x0bterm_number\x18\x04 \x01(\x12\x12\x16\n\x07vote_id\x18\x05 \x01(\x0b\x32\x05.Hash\x12\x11\n\tlock_time\x18\x07 \x01(\x12\x12\x34\n\x10unlock_timestamp\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x12withdraw_timestamp\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0evote_timestamp\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cis_withdrawn\x18\r \x01(\x08\"\xa7\x02\n\x0b\x45lectorVote\x12\'\n\x18\x61\x63tive_voting_record_ids\x18\x01 \x03(\x0b\x32\x05.Hash\x12*\n\x1bwithdrawn_voting_record_ids\x18\x02 \x03(\x0b\x32\x05.Hash\x12!\n\x19\x61\x63tive_voted_votes_amount\x18\x03 \x01(\x12\x12\x1e\n\x16\x61ll_voted_votes_amount\x18\x04 \x01(\x12\x12\x34\n\x15\x61\x63tive_voting_records\x18\x05 \x03(\x0b\x32\x15.ElectionVotingRecord\x12\x36\n\x17withdrawn_votes_records\x18\x06 \x03(\x0b\x32\x15.ElectionVotingRecord\x12\x12\n\npublic_key\x18\x07 \x01(\x0c\"\xdf\x02\n\rCandidateVote\x12\x30\n!obtained_active_voting_record_ids\x18\x01 \x03(\x0b\x32\x05.Hash\x12\x33\n$obtained_withdrawn_voting_record_ids\x18\x02 \x03(\x0b\x32\x05.Hash\x12*\n\"obtained_active_voted_votes_amount\x18\x03 \x01(\x12\x12\'\n\x1f\x61ll_obtained_voted_votes_amount\x18\x04 \x01(\x12\x12=\n\x1eobtained_active_voting_records\x18\x05 \x03(\x0b\x32\x15.ElectionVotingRecord\x12?\n obtained_withdrawn_votes_records\x18\x06 \x03(\x0b\x32\x15.ElectionVotingRecord\x12\x12\n\npublic_key\x18\x07 \x01(\x0c\"\x1f\n\x0ePublicKeysList\x12\r\n\x05value\x18\x01 \x03(\x0c\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_STRINGINPUT = _descriptor.Descriptor(
  name='StringInput',
  full_name='StringInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='StringValue', full_name='StringInput.StringValue', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=48,
  serialized_end=82,
)


_MINERLIST = _descriptor.Descriptor(
  name='MinerList',
  full_name='MinerList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_keys', full_name='MinerList.public_keys', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=84,
  serialized_end=116,
)


_HASH = _descriptor.Descriptor(
  name='Hash',
  full_name='Hash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Value', full_name='Hash.Value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=118,
  serialized_end=139,
)


_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Value', full_name='Address.Value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=141,
  serialized_end=165,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='From', full_name='Transaction.From', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='To', full_name='Transaction.To', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RefBlockNumber', full_name='Transaction.RefBlockNumber', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RefBlockPrefix', full_name='Transaction.RefBlockPrefix', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MethodName', full_name='Transaction.MethodName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Params', full_name='Transaction.Params', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Signature', full_name='Transaction.Signature', index=6,
      number=10000, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=168,
  serialized_end=331,
)


_ELECTIONVOTINGRECORD = _descriptor.Descriptor(
  name='ElectionVotingRecord',
  full_name='ElectionVotingRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='voter', full_name='ElectionVotingRecord.voter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candidate', full_name='ElectionVotingRecord.candidate', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='ElectionVotingRecord.amount', index=2,
      number=3, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='term_number', full_name='ElectionVotingRecord.term_number', index=3,
      number=4, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vote_id', full_name='ElectionVotingRecord.vote_id', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lock_time', full_name='ElectionVotingRecord.lock_time', index=5,
      number=7, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlock_timestamp', full_name='ElectionVotingRecord.unlock_timestamp', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withdraw_timestamp', full_name='ElectionVotingRecord.withdraw_timestamp', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vote_timestamp', full_name='ElectionVotingRecord.vote_timestamp', index=8,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_withdrawn', full_name='ElectionVotingRecord.is_withdrawn', index=9,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=334,
  serialized_end=664,
)


_ELECTORVOTE = _descriptor.Descriptor(
  name='ElectorVote',
  full_name='ElectorVote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='active_voting_record_ids', full_name='ElectorVote.active_voting_record_ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withdrawn_voting_record_ids', full_name='ElectorVote.withdrawn_voting_record_ids', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active_voted_votes_amount', full_name='ElectorVote.active_voted_votes_amount', index=2,
      number=3, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_voted_votes_amount', full_name='ElectorVote.all_voted_votes_amount', index=3,
      number=4, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active_voting_records', full_name='ElectorVote.active_voting_records', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withdrawn_votes_records', full_name='ElectorVote.withdrawn_votes_records', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='ElectorVote.public_key', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=667,
  serialized_end=962,
)


_CANDIDATEVOTE = _descriptor.Descriptor(
  name='CandidateVote',
  full_name='CandidateVote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='obtained_active_voting_record_ids', full_name='CandidateVote.obtained_active_voting_record_ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obtained_withdrawn_voting_record_ids', full_name='CandidateVote.obtained_withdrawn_voting_record_ids', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obtained_active_voted_votes_amount', full_name='CandidateVote.obtained_active_voted_votes_amount', index=2,
      number=3, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_obtained_voted_votes_amount', full_name='CandidateVote.all_obtained_voted_votes_amount', index=3,
      number=4, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obtained_active_voting_records', full_name='CandidateVote.obtained_active_voting_records', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obtained_withdrawn_votes_records', full_name='CandidateVote.obtained_withdrawn_votes_records', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='CandidateVote.public_key', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=965,
  serialized_end=1316,
)


_PUBLICKEYSLIST = _descriptor.Descriptor(
  name='PublicKeysList',
  full_name='PublicKeysList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='PublicKeysList.value', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=1318,
  serialized_end=1349,
)

_TRANSACTION.fields_by_name['From'].message_type = _ADDRESS
_TRANSACTION.fields_by_name['To'].message_type = _ADDRESS
_ELECTIONVOTINGRECORD.fields_by_name['voter'].message_type = _ADDRESS
_ELECTIONVOTINGRECORD.fields_by_name['vote_id'].message_type = _HASH
_ELECTIONVOTINGRECORD.fields_by_name['unlock_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ELECTIONVOTINGRECORD.fields_by_name['withdraw_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ELECTIONVOTINGRECORD.fields_by_name['vote_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ELECTORVOTE.fields_by_name['active_voting_record_ids'].message_type = _HASH
_ELECTORVOTE.fields_by_name['withdrawn_voting_record_ids'].message_type = _HASH
_ELECTORVOTE.fields_by_name['active_voting_records'].message_type = _ELECTIONVOTINGRECORD
_ELECTORVOTE.fields_by_name['withdrawn_votes_records'].message_type = _ELECTIONVOTINGRECORD
_CANDIDATEVOTE.fields_by_name['obtained_active_voting_record_ids'].message_type = _HASH
_CANDIDATEVOTE.fields_by_name['obtained_withdrawn_voting_record_ids'].message_type = _HASH
_CANDIDATEVOTE.fields_by_name['obtained_active_voting_records'].message_type = _ELECTIONVOTINGRECORD
_CANDIDATEVOTE.fields_by_name['obtained_withdrawn_votes_records'].message_type = _ELECTIONVOTINGRECORD
DESCRIPTOR.message_types_by_name['StringInput'] = _STRINGINPUT
DESCRIPTOR.message_types_by_name['MinerList'] = _MINERLIST
DESCRIPTOR.message_types_by_name['Hash'] = _HASH
DESCRIPTOR.message_types_by_name['Address'] = _ADDRESS
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['ElectionVotingRecord'] = _ELECTIONVOTINGRECORD
DESCRIPTOR.message_types_by_name['ElectorVote'] = _ELECTORVOTE
DESCRIPTOR.message_types_by_name['CandidateVote'] = _CANDIDATEVOTE
DESCRIPTOR.message_types_by_name['PublicKeysList'] = _PUBLICKEYSLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StringInput = _reflection.GeneratedProtocolMessageType('StringInput', (_message.Message,), dict(
  DESCRIPTOR = _STRINGINPUT,
  __module__ = 'types_pb2'
  # @@protoc_insertion_point(class_scope:StringInput)
  ))
_sym_db.RegisterMessage(StringInput)

MinerList = _reflection.GeneratedProtocolMessageType('MinerList', (_message.Message,), dict(
  DESCRIPTOR = _MINERLIST,
  __module__ = 'types_pb2'
  # @@protoc_insertion_point(class_scope:MinerList)
  ))
_sym_db.RegisterMessage(MinerList)

Hash = _reflection.GeneratedProtocolMessageType('Hash', (_message.Message,), dict(
  DESCRIPTOR = _HASH,
  __module__ = 'types_pb2'
  # @@protoc_insertion_point(class_scope:Hash)
  ))
_sym_db.RegisterMessage(Hash)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESS,
  __module__ = 'types_pb2'
  # @@protoc_insertion_point(class_scope:Address)
  ))
_sym_db.RegisterMessage(Address)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'types_pb2'
  # @@protoc_insertion_point(class_scope:Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

ElectionVotingRecord = _reflection.GeneratedProtocolMessageType('ElectionVotingRecord', (_message.Message,), dict(
  DESCRIPTOR = _ELECTIONVOTINGRECORD,
  __module__ = 'types_pb2'
  # @@protoc_insertion_point(class_scope:ElectionVotingRecord)
  ))
_sym_db.RegisterMessage(ElectionVotingRecord)

ElectorVote = _reflection.GeneratedProtocolMessageType('ElectorVote', (_message.Message,), dict(
  DESCRIPTOR = _ELECTORVOTE,
  __module__ = 'types_pb2'
  # @@protoc_insertion_point(class_scope:ElectorVote)
  ))
_sym_db.RegisterMessage(ElectorVote)

CandidateVote = _reflection.GeneratedProtocolMessageType('CandidateVote', (_message.Message,), dict(
  DESCRIPTOR = _CANDIDATEVOTE,
  __module__ = 'types_pb2'
  # @@protoc_insertion_point(class_scope:CandidateVote)
  ))
_sym_db.RegisterMessage(CandidateVote)

PublicKeysList = _reflection.GeneratedProtocolMessageType('PublicKeysList', (_message.Message,), dict(
  DESCRIPTOR = _PUBLICKEYSLIST,
  __module__ = 'types_pb2'
  # @@protoc_insertion_point(class_scope:PublicKeysList)
  ))
_sym_db.RegisterMessage(PublicKeysList)


# @@protoc_insertion_point(module_scope)
