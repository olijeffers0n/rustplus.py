# -*- coding: utf-8 -*-
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rustplus.proto',
  package='rustplus',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0erustplus.proto\x12\x08rustplus\"`\n\nAppMessage\x12\'\n\x08response\x18\x01 \x01(\x0b\x32\x15.rustplus.AppResponse\x12)\n\tbroadcast\x18\x02 \x01(\x0b\x32\x16.rustplus.AppBroadcast\"\x9b\x05\n\nAppRequest\x12\x0b\n\x03seq\x18\x01 \x02(\r\x12\x10\n\x08playerId\x18\x02 \x02(\x04\x12\x13\n\x0bplayerToken\x18\x03 \x02(\x05\x12\x10\n\x08\x65ntityId\x18\x04 \x01(\r\x12#\n\x07getInfo\x18\x08 \x01(\x0b\x32\x12.rustplus.AppEmpty\x12#\n\x07getTime\x18\t \x01(\x0b\x32\x12.rustplus.AppEmpty\x12\"\n\x06getMap\x18\n \x01(\x0b\x32\x12.rustplus.AppEmpty\x12\'\n\x0bgetTeamInfo\x18\x0b \x01(\x0b\x32\x12.rustplus.AppEmpty\x12\'\n\x0bgetTeamChat\x18\x0c \x01(\x0b\x32\x12.rustplus.AppEmpty\x12\x31\n\x0fsendTeamMessage\x18\r \x01(\x0b\x32\x18.rustplus.AppSendMessage\x12)\n\rgetEntityInfo\x18\x0e \x01(\x0b\x32\x12.rustplus.AppEmpty\x12\x33\n\x0esetEntityValue\x18\x0f \x01(\x0b\x32\x1b.rustplus.AppSetEntityValue\x12-\n\x11\x63heckSubscription\x18\x10 \x01(\x0b\x32\x12.rustplus.AppEmpty\x12*\n\x0fsetSubscription\x18\x11 \x01(\x0b\x32\x11.rustplus.AppFlag\x12)\n\rgetMapMarkers\x18\x12 \x01(\x0b\x32\x12.rustplus.AppEmpty\x12\x37\n\x0egetCameraFrame\x18\x13 \x01(\x0b\x32\x1f.rustplus.AppCameraFrameRequest\x12\x35\n\x0fpromoteToLeader\x18\x14 \x01(\x0b\x32\x1c.rustplus.AppPromoteToLeader\"!\n\x0e\x41ppSendMessage\x12\x0f\n\x07message\x18\x01 \x02(\t\"\"\n\x11\x41ppSetEntityValue\x12\r\n\x05value\x18\x01 \x02(\x08\":\n\x15\x41ppCameraFrameRequest\x12\x12\n\nidentifier\x18\x01 \x02(\t\x12\r\n\x05\x66rame\x18\x02 \x02(\r\"%\n\x12\x41ppPromoteToLeader\x12\x0f\n\x07steamId\x18\x01 \x02(\x04\"\xc1\x03\n\x0b\x41ppResponse\x12\x0b\n\x03seq\x18\x01 \x02(\r\x12%\n\x07success\x18\x04 \x01(\x0b\x32\x14.rustplus.AppSuccess\x12!\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x12.rustplus.AppError\x12\x1f\n\x04info\x18\x06 \x01(\x0b\x32\x11.rustplus.AppInfo\x12\x1f\n\x04time\x18\x07 \x01(\x0b\x32\x11.rustplus.AppTime\x12\x1d\n\x03map\x18\x08 \x01(\x0b\x32\x10.rustplus.AppMap\x12\'\n\x08teamInfo\x18\t \x01(\x0b\x32\x15.rustplus.AppTeamInfo\x12\'\n\x08teamChat\x18\n \x01(\x0b\x32\x15.rustplus.AppTeamChat\x12+\n\nentityInfo\x18\x0b \x01(\x0b\x32\x17.rustplus.AppEntityInfo\x12\x1f\n\x04\x66lag\x18\x0c \x01(\x0b\x32\x11.rustplus.AppFlag\x12+\n\nmapMarkers\x18\r \x01(\x0b\x32\x17.rustplus.AppMapMarkers\x12-\n\x0b\x63\x61meraFrame\x18\x0e \x01(\x0b\x32\x18.rustplus.AppCameraFrame\"\x9f\x01\n\x0c\x41ppBroadcast\x12-\n\x0bteamChanged\x18\x04 \x01(\x0b\x32\x18.rustplus.AppTeamChanged\x12-\n\x0bteamMessage\x18\x05 \x01(\x0b\x32\x18.rustplus.AppTeamMessage\x12\x31\n\rentityChanged\x18\x06 \x01(\x0b\x32\x1a.rustplus.AppEntityChanged\"\n\n\x08\x41ppEmpty\"\x0c\n\nAppSuccess\"\x19\n\x08\x41ppError\x12\r\n\x05\x65rror\x18\x01 \x02(\t\"\xc1\x01\n\x07\x41ppInfo\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x13\n\x0bheaderImage\x18\x02 \x02(\t\x12\x0b\n\x03url\x18\x03 \x02(\t\x12\x0b\n\x03map\x18\x04 \x02(\t\x12\x0f\n\x07mapSize\x18\x05 \x02(\r\x12\x10\n\x08wipeTime\x18\x06 \x02(\r\x12\x0f\n\x07players\x18\x07 \x02(\r\x12\x12\n\nmaxPlayers\x18\x08 \x02(\r\x12\x15\n\rqueuedPlayers\x18\t \x02(\r\x12\x0c\n\x04seed\x18\n \x01(\r\x12\x0c\n\x04salt\x18\x0b \x01(\r\"e\n\x07\x41ppTime\x12\x18\n\x10\x64\x61yLengthMinutes\x18\x01 \x02(\x02\x12\x11\n\ttimeScale\x18\x02 \x02(\x02\x12\x0f\n\x07sunrise\x18\x03 \x02(\x02\x12\x0e\n\x06sunset\x18\x04 \x02(\x02\x12\x0c\n\x04time\x18\x05 \x02(\x02\"\xc1\x01\n\x06\x41ppMap\x12\r\n\x05width\x18\x01 \x02(\r\x12\x0e\n\x06height\x18\x02 \x02(\r\x12\x10\n\x08jpgImage\x18\x03 \x02(\x0c\x12\x13\n\x0boceanMargin\x18\x04 \x02(\x05\x12,\n\tmonuments\x18\x05 \x03(\x0b\x32\x19.rustplus.AppMap.Monument\x12\x12\n\nbackground\x18\x06 \x01(\t\x1a/\n\x08Monument\x12\r\n\x05token\x18\x01 \x02(\t\x12\t\n\x01x\x18\x02 \x02(\x02\x12\t\n\x01y\x18\x03 \x02(\x02\"\xea\x02\n\x0b\x41ppTeamInfo\x12\x15\n\rleaderSteamId\x18\x01 \x02(\x04\x12-\n\x07members\x18\x02 \x03(\x0b\x32\x1c.rustplus.AppTeamInfo.Member\x12,\n\x08mapNotes\x18\x03 \x03(\x0b\x32\x1a.rustplus.AppTeamInfo.Note\x12\x32\n\x0eleaderMapNotes\x18\x04 \x03(\x0b\x32\x1a.rustplus.AppTeamInfo.Note\x1a\x86\x01\n\x06Member\x12\x0f\n\x07steamId\x18\x01 \x02(\x04\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\t\n\x01x\x18\x03 \x02(\x02\x12\t\n\x01y\x18\x04 \x02(\x02\x12\x10\n\x08isOnline\x18\x05 \x02(\x08\x12\x11\n\tspawnTime\x18\x06 \x02(\r\x12\x0f\n\x07isAlive\x18\x07 \x02(\x08\x12\x11\n\tdeathTime\x18\x08 \x02(\r\x1a*\n\x04Note\x12\x0c\n\x04type\x18\x02 \x02(\x05\x12\t\n\x01x\x18\x03 \x02(\x02\x12\t\n\x01y\x18\x04 \x02(\x02\"9\n\x0b\x41ppTeamChat\x12*\n\x08messages\x18\x01 \x03(\x0b\x32\x18.rustplus.AppChatMessage\"]\n\x0e\x41ppChatMessage\x12\x0f\n\x07steamId\x18\x01 \x02(\x04\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0f\n\x07message\x18\x03 \x02(\t\x12\r\n\x05\x63olor\x18\x04 \x02(\t\x12\x0c\n\x04time\x18\x05 \x02(\r\"c\n\rAppEntityInfo\x12%\n\x04type\x18\x01 \x02(\x0e\x32\x17.rustplus.AppEntityType\x12+\n\x07payload\x18\x03 \x02(\x0b\x32\x1a.rustplus.AppEntityPayload\"\xd7\x01\n\x10\x41ppEntityPayload\x12\r\n\x05value\x18\x01 \x01(\x08\x12.\n\x05items\x18\x02 \x03(\x0b\x32\x1f.rustplus.AppEntityPayload.Item\x12\x10\n\x08\x63\x61pacity\x18\x03 \x01(\x05\x12\x15\n\rhasProtection\x18\x04 \x01(\x08\x12\x18\n\x10protectionExpiry\x18\x05 \x01(\r\x1a\x41\n\x04Item\x12\x0e\n\x06itemId\x18\x01 \x02(\x05\x12\x10\n\x08quantity\x18\x02 \x02(\x05\x12\x17\n\x0fitemIsBlueprint\x18\x03 \x02(\x08\"\x18\n\x07\x41ppFlag\x12\r\n\x05value\x18\x01 \x02(\x08\"5\n\rAppMapMarkers\x12$\n\x07markers\x18\x01 \x03(\x0b\x32\x13.rustplus.AppMarker\"5\n\x07Vector4\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\t\n\x01w\x18\x04 \x01(\x02\"\xc3\x03\n\tAppMarker\x12\n\n\x02id\x18\x01 \x02(\r\x12%\n\x04type\x18\x02 \x02(\x0e\x32\x17.rustplus.AppMarkerType\x12\t\n\x01x\x18\x03 \x02(\x02\x12\t\n\x01y\x18\x04 \x02(\x02\x12\x0f\n\x07steamId\x18\x05 \x01(\x04\x12\x10\n\x08rotation\x18\x06 \x01(\x02\x12\x0e\n\x06radius\x18\x07 \x01(\x02\x12!\n\x06\x63olor1\x18\x08 \x01(\x0b\x32\x11.rustplus.Vector4\x12!\n\x06\x63olor2\x18\t \x01(\x0b\x32\x11.rustplus.Vector4\x12\r\n\x05\x61lpha\x18\n \x01(\x02\x12\x0c\n\x04name\x18\x0b \x01(\t\x12\x31\n\nsellOrders\x18\r \x03(\x0b\x32\x1d.rustplus.AppMarker.SellOrder\x1a\xa3\x01\n\tSellOrder\x12\x0e\n\x06itemId\x18\x01 \x02(\x05\x12\x10\n\x08quantity\x18\x02 \x02(\x05\x12\x12\n\ncurrencyId\x18\x03 \x02(\x05\x12\x13\n\x0b\x63ostPerItem\x18\x04 \x02(\x05\x12\x15\n\ramountInStock\x18\x05 \x02(\x05\x12\x17\n\x0fitemIsBlueprint\x18\x06 \x02(\x08\x12\x1b\n\x13\x63urrencyIsBlueprint\x18\x07 \x02(\x08\"1\n\x0e\x41ppCameraFrame\x12\r\n\x05\x66rame\x18\x01 \x02(\r\x12\x10\n\x08jpgImage\x18\x02 \x02(\x0c\"K\n\x0e\x41ppTeamChanged\x12\x10\n\x08playerId\x18\x01 \x02(\x04\x12\'\n\x08teamInfo\x18\x02 \x02(\x0b\x32\x15.rustplus.AppTeamInfo\";\n\x0e\x41ppTeamMessage\x12)\n\x07message\x18\x01 \x02(\x0b\x32\x18.rustplus.AppChatMessage\"Q\n\x10\x41ppEntityChanged\x12\x10\n\x08\x65ntityId\x18\x01 \x02(\r\x12+\n\x07payload\x18\x02 \x02(\x0b\x32\x1a.rustplus.AppEntityPayload*:\n\rAppEntityType\x12\n\n\x06Switch\x10\x01\x12\t\n\x05\x41larm\x10\x02\x12\x12\n\x0eStorageMonitor\x10\x03*u\n\rAppMarkerType\x12\n\n\x06Player\x10\x01\x12\r\n\tExplosion\x10\x02\x12\x12\n\x0eVendingMachine\x10\x03\x12\x08\n\x04\x43H47\x10\x04\x12\r\n\tCargoShip\x10\x05\x12\t\n\x05\x43rate\x10\x06\x12\x11\n\rGenericRadius\x10\x07'
)

_APPENTITYTYPE = _descriptor.EnumDescriptor(
  name='AppEntityType',
  full_name='rustplus.AppEntityType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Switch', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Alarm', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='StorageMonitor', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=3828,
  serialized_end=3886,
)
_sym_db.RegisterEnumDescriptor(_APPENTITYTYPE)

AppEntityType = enum_type_wrapper.EnumTypeWrapper(_APPENTITYTYPE)
_APPMARKERTYPE = _descriptor.EnumDescriptor(
  name='AppMarkerType',
  full_name='rustplus.AppMarkerType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Player', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Explosion', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VendingMachine', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CH47', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CargoShip', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Crate', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GenericRadius', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=3888,
  serialized_end=4005,
)
_sym_db.RegisterEnumDescriptor(_APPMARKERTYPE)

AppMarkerType = enum_type_wrapper.EnumTypeWrapper(_APPMARKERTYPE)
Switch = 1
Alarm = 2
StorageMonitor = 3
Player = 1
Explosion = 2
VendingMachine = 3
CH47 = 4
CargoShip = 5
Crate = 6
GenericRadius = 7



_APPMESSAGE = _descriptor.Descriptor(
  name='AppMessage',
  full_name='rustplus.AppMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='rustplus.AppMessage.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='broadcast', full_name='rustplus.AppMessage.broadcast', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=124,
)


_APPREQUEST = _descriptor.Descriptor(
  name='AppRequest',
  full_name='rustplus.AppRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='seq', full_name='rustplus.AppRequest.seq', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playerId', full_name='rustplus.AppRequest.playerId', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playerToken', full_name='rustplus.AppRequest.playerToken', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entityId', full_name='rustplus.AppRequest.entityId', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='getInfo', full_name='rustplus.AppRequest.getInfo', index=4,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='getTime', full_name='rustplus.AppRequest.getTime', index=5,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='getMap', full_name='rustplus.AppRequest.getMap', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='getTeamInfo', full_name='rustplus.AppRequest.getTeamInfo', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='getTeamChat', full_name='rustplus.AppRequest.getTeamChat', index=8,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sendTeamMessage', full_name='rustplus.AppRequest.sendTeamMessage', index=9,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='getEntityInfo', full_name='rustplus.AppRequest.getEntityInfo', index=10,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='setEntityValue', full_name='rustplus.AppRequest.setEntityValue', index=11,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='checkSubscription', full_name='rustplus.AppRequest.checkSubscription', index=12,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='setSubscription', full_name='rustplus.AppRequest.setSubscription', index=13,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='getMapMarkers', full_name='rustplus.AppRequest.getMapMarkers', index=14,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='getCameraFrame', full_name='rustplus.AppRequest.getCameraFrame', index=15,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='promoteToLeader', full_name='rustplus.AppRequest.promoteToLeader', index=16,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=794,
)


_APPSENDMESSAGE = _descriptor.Descriptor(
  name='AppSendMessage',
  full_name='rustplus.AppSendMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='rustplus.AppSendMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=796,
  serialized_end=829,
)


_APPSETENTITYVALUE = _descriptor.Descriptor(
  name='AppSetEntityValue',
  full_name='rustplus.AppSetEntityValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='rustplus.AppSetEntityValue.value', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=831,
  serialized_end=865,
)


_APPCAMERAFRAMEREQUEST = _descriptor.Descriptor(
  name='AppCameraFrameRequest',
  full_name='rustplus.AppCameraFrameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='rustplus.AppCameraFrameRequest.identifier', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frame', full_name='rustplus.AppCameraFrameRequest.frame', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=867,
  serialized_end=925,
)


_APPPROMOTETOLEADER = _descriptor.Descriptor(
  name='AppPromoteToLeader',
  full_name='rustplus.AppPromoteToLeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='steamId', full_name='rustplus.AppPromoteToLeader.steamId', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=927,
  serialized_end=964,
)


_APPRESPONSE = _descriptor.Descriptor(
  name='AppResponse',
  full_name='rustplus.AppResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='seq', full_name='rustplus.AppResponse.seq', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='success', full_name='rustplus.AppResponse.success', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='rustplus.AppResponse.error', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='rustplus.AppResponse.info', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='rustplus.AppResponse.time', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='map', full_name='rustplus.AppResponse.map', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teamInfo', full_name='rustplus.AppResponse.teamInfo', index=6,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teamChat', full_name='rustplus.AppResponse.teamChat', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entityInfo', full_name='rustplus.AppResponse.entityInfo', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flag', full_name='rustplus.AppResponse.flag', index=9,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mapMarkers', full_name='rustplus.AppResponse.mapMarkers', index=10,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cameraFrame', full_name='rustplus.AppResponse.cameraFrame', index=11,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=967,
  serialized_end=1416,
)


_APPBROADCAST = _descriptor.Descriptor(
  name='AppBroadcast',
  full_name='rustplus.AppBroadcast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='teamChanged', full_name='rustplus.AppBroadcast.teamChanged', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teamMessage', full_name='rustplus.AppBroadcast.teamMessage', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entityChanged', full_name='rustplus.AppBroadcast.entityChanged', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1419,
  serialized_end=1578,
)


_APPEMPTY = _descriptor.Descriptor(
  name='AppEmpty',
  full_name='rustplus.AppEmpty',
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1580,
  serialized_end=1590,
)


_APPSUCCESS = _descriptor.Descriptor(
  name='AppSuccess',
  full_name='rustplus.AppSuccess',
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1592,
  serialized_end=1604,
)


_APPERROR = _descriptor.Descriptor(
  name='AppError',
  full_name='rustplus.AppError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='rustplus.AppError.error', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1606,
  serialized_end=1631,
)


_APPINFO = _descriptor.Descriptor(
  name='AppInfo',
  full_name='rustplus.AppInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rustplus.AppInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='headerImage', full_name='rustplus.AppInfo.headerImage', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='rustplus.AppInfo.url', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='map', full_name='rustplus.AppInfo.map', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mapSize', full_name='rustplus.AppInfo.mapSize', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wipeTime', full_name='rustplus.AppInfo.wipeTime', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='players', full_name='rustplus.AppInfo.players', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maxPlayers', full_name='rustplus.AppInfo.maxPlayers', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queuedPlayers', full_name='rustplus.AppInfo.queuedPlayers', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seed', full_name='rustplus.AppInfo.seed', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='salt', full_name='rustplus.AppInfo.salt', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1634,
  serialized_end=1827,
)


_APPTIME = _descriptor.Descriptor(
  name='AppTime',
  full_name='rustplus.AppTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dayLengthMinutes', full_name='rustplus.AppTime.dayLengthMinutes', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeScale', full_name='rustplus.AppTime.timeScale', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sunrise', full_name='rustplus.AppTime.sunrise', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sunset', full_name='rustplus.AppTime.sunset', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='rustplus.AppTime.time', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1829,
  serialized_end=1930,
)


_APPMAP_MONUMENT = _descriptor.Descriptor(
  name='Monument',
  full_name='rustplus.AppMap.Monument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='rustplus.AppMap.Monument.token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='rustplus.AppMap.Monument.x', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='rustplus.AppMap.Monument.y', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2079,
  serialized_end=2126,
)

_APPMAP = _descriptor.Descriptor(
  name='AppMap',
  full_name='rustplus.AppMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='rustplus.AppMap.width', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='rustplus.AppMap.height', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jpgImage', full_name='rustplus.AppMap.jpgImage', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oceanMargin', full_name='rustplus.AppMap.oceanMargin', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monuments', full_name='rustplus.AppMap.monuments', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='background', full_name='rustplus.AppMap.background', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_APPMAP_MONUMENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1933,
  serialized_end=2126,
)


_APPTEAMINFO_MEMBER = _descriptor.Descriptor(
  name='Member',
  full_name='rustplus.AppTeamInfo.Member',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='steamId', full_name='rustplus.AppTeamInfo.Member.steamId', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='rustplus.AppTeamInfo.Member.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='rustplus.AppTeamInfo.Member.x', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='rustplus.AppTeamInfo.Member.y', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isOnline', full_name='rustplus.AppTeamInfo.Member.isOnline', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spawnTime', full_name='rustplus.AppTeamInfo.Member.spawnTime', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isAlive', full_name='rustplus.AppTeamInfo.Member.isAlive', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deathTime', full_name='rustplus.AppTeamInfo.Member.deathTime', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2313,
  serialized_end=2447,
)

_APPTEAMINFO_NOTE = _descriptor.Descriptor(
  name='Note',
  full_name='rustplus.AppTeamInfo.Note',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='rustplus.AppTeamInfo.Note.type', index=0,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='rustplus.AppTeamInfo.Note.x', index=1,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='rustplus.AppTeamInfo.Note.y', index=2,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2449,
  serialized_end=2491,
)

_APPTEAMINFO = _descriptor.Descriptor(
  name='AppTeamInfo',
  full_name='rustplus.AppTeamInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='leaderSteamId', full_name='rustplus.AppTeamInfo.leaderSteamId', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='members', full_name='rustplus.AppTeamInfo.members', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mapNotes', full_name='rustplus.AppTeamInfo.mapNotes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leaderMapNotes', full_name='rustplus.AppTeamInfo.leaderMapNotes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_APPTEAMINFO_MEMBER, _APPTEAMINFO_NOTE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2129,
  serialized_end=2491,
)


_APPTEAMCHAT = _descriptor.Descriptor(
  name='AppTeamChat',
  full_name='rustplus.AppTeamChat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='rustplus.AppTeamChat.messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2493,
  serialized_end=2550,
)


_APPCHATMESSAGE = _descriptor.Descriptor(
  name='AppChatMessage',
  full_name='rustplus.AppChatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='steamId', full_name='rustplus.AppChatMessage.steamId', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='rustplus.AppChatMessage.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='rustplus.AppChatMessage.message', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='rustplus.AppChatMessage.color', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='rustplus.AppChatMessage.time', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2552,
  serialized_end=2645,
)


_APPENTITYINFO = _descriptor.Descriptor(
  name='AppEntityInfo',
  full_name='rustplus.AppEntityInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='rustplus.AppEntityInfo.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='rustplus.AppEntityInfo.payload', index=1,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2647,
  serialized_end=2746,
)


_APPENTITYPAYLOAD_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='rustplus.AppEntityPayload.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='itemId', full_name='rustplus.AppEntityPayload.Item.itemId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='rustplus.AppEntityPayload.Item.quantity', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemIsBlueprint', full_name='rustplus.AppEntityPayload.Item.itemIsBlueprint', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2899,
  serialized_end=2964,
)

_APPENTITYPAYLOAD = _descriptor.Descriptor(
  name='AppEntityPayload',
  full_name='rustplus.AppEntityPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='rustplus.AppEntityPayload.value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='rustplus.AppEntityPayload.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='capacity', full_name='rustplus.AppEntityPayload.capacity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hasProtection', full_name='rustplus.AppEntityPayload.hasProtection', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protectionExpiry', full_name='rustplus.AppEntityPayload.protectionExpiry', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_APPENTITYPAYLOAD_ITEM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2749,
  serialized_end=2964,
)


_APPFLAG = _descriptor.Descriptor(
  name='AppFlag',
  full_name='rustplus.AppFlag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='rustplus.AppFlag.value', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2966,
  serialized_end=2990,
)


_APPMAPMARKERS = _descriptor.Descriptor(
  name='AppMapMarkers',
  full_name='rustplus.AppMapMarkers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='markers', full_name='rustplus.AppMapMarkers.markers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2992,
  serialized_end=3045,
)


_VECTOR4 = _descriptor.Descriptor(
  name='Vector4',
  full_name='rustplus.Vector4',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='rustplus.Vector4.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='rustplus.Vector4.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='rustplus.Vector4.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='w', full_name='rustplus.Vector4.w', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3047,
  serialized_end=3100,
)


_APPMARKER_SELLORDER = _descriptor.Descriptor(
  name='SellOrder',
  full_name='rustplus.AppMarker.SellOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='itemId', full_name='rustplus.AppMarker.SellOrder.itemId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='rustplus.AppMarker.SellOrder.quantity', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currencyId', full_name='rustplus.AppMarker.SellOrder.currencyId', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='costPerItem', full_name='rustplus.AppMarker.SellOrder.costPerItem', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amountInStock', full_name='rustplus.AppMarker.SellOrder.amountInStock', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='itemIsBlueprint', full_name='rustplus.AppMarker.SellOrder.itemIsBlueprint', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currencyIsBlueprint', full_name='rustplus.AppMarker.SellOrder.currencyIsBlueprint', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3391,
  serialized_end=3554,
)

_APPMARKER = _descriptor.Descriptor(
  name='AppMarker',
  full_name='rustplus.AppMarker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rustplus.AppMarker.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='rustplus.AppMarker.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='rustplus.AppMarker.x', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='rustplus.AppMarker.y', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='steamId', full_name='rustplus.AppMarker.steamId', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='rustplus.AppMarker.rotation', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='radius', full_name='rustplus.AppMarker.radius', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color1', full_name='rustplus.AppMarker.color1', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color2', full_name='rustplus.AppMarker.color2', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alpha', full_name='rustplus.AppMarker.alpha', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='rustplus.AppMarker.name', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sellOrders', full_name='rustplus.AppMarker.sellOrders', index=11,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_APPMARKER_SELLORDER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3103,
  serialized_end=3554,
)


_APPCAMERAFRAME = _descriptor.Descriptor(
  name='AppCameraFrame',
  full_name='rustplus.AppCameraFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame', full_name='rustplus.AppCameraFrame.frame', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jpgImage', full_name='rustplus.AppCameraFrame.jpgImage', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3556,
  serialized_end=3605,
)


_APPTEAMCHANGED = _descriptor.Descriptor(
  name='AppTeamChanged',
  full_name='rustplus.AppTeamChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerId', full_name='rustplus.AppTeamChanged.playerId', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teamInfo', full_name='rustplus.AppTeamChanged.teamInfo', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3607,
  serialized_end=3682,
)


_APPTEAMMESSAGE = _descriptor.Descriptor(
  name='AppTeamMessage',
  full_name='rustplus.AppTeamMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='rustplus.AppTeamMessage.message', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3684,
  serialized_end=3743,
)


_APPENTITYCHANGED = _descriptor.Descriptor(
  name='AppEntityChanged',
  full_name='rustplus.AppEntityChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entityId', full_name='rustplus.AppEntityChanged.entityId', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='rustplus.AppEntityChanged.payload', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3745,
  serialized_end=3826,
)

_APPMESSAGE.fields_by_name['response'].message_type = _APPRESPONSE
_APPMESSAGE.fields_by_name['broadcast'].message_type = _APPBROADCAST
_APPREQUEST.fields_by_name['getInfo'].message_type = _APPEMPTY
_APPREQUEST.fields_by_name['getTime'].message_type = _APPEMPTY
_APPREQUEST.fields_by_name['getMap'].message_type = _APPEMPTY
_APPREQUEST.fields_by_name['getTeamInfo'].message_type = _APPEMPTY
_APPREQUEST.fields_by_name['getTeamChat'].message_type = _APPEMPTY
_APPREQUEST.fields_by_name['sendTeamMessage'].message_type = _APPSENDMESSAGE
_APPREQUEST.fields_by_name['getEntityInfo'].message_type = _APPEMPTY
_APPREQUEST.fields_by_name['setEntityValue'].message_type = _APPSETENTITYVALUE
_APPREQUEST.fields_by_name['checkSubscription'].message_type = _APPEMPTY
_APPREQUEST.fields_by_name['setSubscription'].message_type = _APPFLAG
_APPREQUEST.fields_by_name['getMapMarkers'].message_type = _APPEMPTY
_APPREQUEST.fields_by_name['getCameraFrame'].message_type = _APPCAMERAFRAMEREQUEST
_APPREQUEST.fields_by_name['promoteToLeader'].message_type = _APPPROMOTETOLEADER
_APPRESPONSE.fields_by_name['success'].message_type = _APPSUCCESS
_APPRESPONSE.fields_by_name['error'].message_type = _APPERROR
_APPRESPONSE.fields_by_name['info'].message_type = _APPINFO
_APPRESPONSE.fields_by_name['time'].message_type = _APPTIME
_APPRESPONSE.fields_by_name['map'].message_type = _APPMAP
_APPRESPONSE.fields_by_name['teamInfo'].message_type = _APPTEAMINFO
_APPRESPONSE.fields_by_name['teamChat'].message_type = _APPTEAMCHAT
_APPRESPONSE.fields_by_name['entityInfo'].message_type = _APPENTITYINFO
_APPRESPONSE.fields_by_name['flag'].message_type = _APPFLAG
_APPRESPONSE.fields_by_name['mapMarkers'].message_type = _APPMAPMARKERS
_APPRESPONSE.fields_by_name['cameraFrame'].message_type = _APPCAMERAFRAME
_APPBROADCAST.fields_by_name['teamChanged'].message_type = _APPTEAMCHANGED
_APPBROADCAST.fields_by_name['teamMessage'].message_type = _APPTEAMMESSAGE
_APPBROADCAST.fields_by_name['entityChanged'].message_type = _APPENTITYCHANGED
_APPMAP_MONUMENT.containing_type = _APPMAP
_APPMAP.fields_by_name['monuments'].message_type = _APPMAP_MONUMENT
_APPTEAMINFO_MEMBER.containing_type = _APPTEAMINFO
_APPTEAMINFO_NOTE.containing_type = _APPTEAMINFO
_APPTEAMINFO.fields_by_name['members'].message_type = _APPTEAMINFO_MEMBER
_APPTEAMINFO.fields_by_name['mapNotes'].message_type = _APPTEAMINFO_NOTE
_APPTEAMINFO.fields_by_name['leaderMapNotes'].message_type = _APPTEAMINFO_NOTE
_APPTEAMCHAT.fields_by_name['messages'].message_type = _APPCHATMESSAGE
_APPENTITYINFO.fields_by_name['type'].enum_type = _APPENTITYTYPE
_APPENTITYINFO.fields_by_name['payload'].message_type = _APPENTITYPAYLOAD
_APPENTITYPAYLOAD_ITEM.containing_type = _APPENTITYPAYLOAD
_APPENTITYPAYLOAD.fields_by_name['items'].message_type = _APPENTITYPAYLOAD_ITEM
_APPMAPMARKERS.fields_by_name['markers'].message_type = _APPMARKER
_APPMARKER_SELLORDER.containing_type = _APPMARKER
_APPMARKER.fields_by_name['type'].enum_type = _APPMARKERTYPE
_APPMARKER.fields_by_name['color1'].message_type = _VECTOR4
_APPMARKER.fields_by_name['color2'].message_type = _VECTOR4
_APPMARKER.fields_by_name['sellOrders'].message_type = _APPMARKER_SELLORDER
_APPTEAMCHANGED.fields_by_name['teamInfo'].message_type = _APPTEAMINFO
_APPTEAMMESSAGE.fields_by_name['message'].message_type = _APPCHATMESSAGE
_APPENTITYCHANGED.fields_by_name['payload'].message_type = _APPENTITYPAYLOAD
DESCRIPTOR.message_types_by_name['AppMessage'] = _APPMESSAGE
DESCRIPTOR.message_types_by_name['AppRequest'] = _APPREQUEST
DESCRIPTOR.message_types_by_name['AppSendMessage'] = _APPSENDMESSAGE
DESCRIPTOR.message_types_by_name['AppSetEntityValue'] = _APPSETENTITYVALUE
DESCRIPTOR.message_types_by_name['AppCameraFrameRequest'] = _APPCAMERAFRAMEREQUEST
DESCRIPTOR.message_types_by_name['AppPromoteToLeader'] = _APPPROMOTETOLEADER
DESCRIPTOR.message_types_by_name['AppResponse'] = _APPRESPONSE
DESCRIPTOR.message_types_by_name['AppBroadcast'] = _APPBROADCAST
DESCRIPTOR.message_types_by_name['AppEmpty'] = _APPEMPTY
DESCRIPTOR.message_types_by_name['AppSuccess'] = _APPSUCCESS
DESCRIPTOR.message_types_by_name['AppError'] = _APPERROR
DESCRIPTOR.message_types_by_name['AppInfo'] = _APPINFO
DESCRIPTOR.message_types_by_name['AppTime'] = _APPTIME
DESCRIPTOR.message_types_by_name['AppMap'] = _APPMAP
DESCRIPTOR.message_types_by_name['AppTeamInfo'] = _APPTEAMINFO
DESCRIPTOR.message_types_by_name['AppTeamChat'] = _APPTEAMCHAT
DESCRIPTOR.message_types_by_name['AppChatMessage'] = _APPCHATMESSAGE
DESCRIPTOR.message_types_by_name['AppEntityInfo'] = _APPENTITYINFO
DESCRIPTOR.message_types_by_name['AppEntityPayload'] = _APPENTITYPAYLOAD
DESCRIPTOR.message_types_by_name['AppFlag'] = _APPFLAG
DESCRIPTOR.message_types_by_name['AppMapMarkers'] = _APPMAPMARKERS
DESCRIPTOR.message_types_by_name['Vector4'] = _VECTOR4
DESCRIPTOR.message_types_by_name['AppMarker'] = _APPMARKER
DESCRIPTOR.message_types_by_name['AppCameraFrame'] = _APPCAMERAFRAME
DESCRIPTOR.message_types_by_name['AppTeamChanged'] = _APPTEAMCHANGED
DESCRIPTOR.message_types_by_name['AppTeamMessage'] = _APPTEAMMESSAGE
DESCRIPTOR.message_types_by_name['AppEntityChanged'] = _APPENTITYCHANGED
DESCRIPTOR.enum_types_by_name['AppEntityType'] = _APPENTITYTYPE
DESCRIPTOR.enum_types_by_name['AppMarkerType'] = _APPMARKERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppMessage = _reflection.GeneratedProtocolMessageType('AppMessage', (_message.Message,), {
  'DESCRIPTOR' : _APPMESSAGE,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppMessage)
  })
_sym_db.RegisterMessage(AppMessage)

AppRequest = _reflection.GeneratedProtocolMessageType('AppRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPREQUEST,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppRequest)
  })
_sym_db.RegisterMessage(AppRequest)

AppSendMessage = _reflection.GeneratedProtocolMessageType('AppSendMessage', (_message.Message,), {
  'DESCRIPTOR' : _APPSENDMESSAGE,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppSendMessage)
  })
_sym_db.RegisterMessage(AppSendMessage)

AppSetEntityValue = _reflection.GeneratedProtocolMessageType('AppSetEntityValue', (_message.Message,), {
  'DESCRIPTOR' : _APPSETENTITYVALUE,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppSetEntityValue)
  })
_sym_db.RegisterMessage(AppSetEntityValue)

AppCameraFrameRequest = _reflection.GeneratedProtocolMessageType('AppCameraFrameRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPCAMERAFRAMEREQUEST,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppCameraFrameRequest)
  })
_sym_db.RegisterMessage(AppCameraFrameRequest)

AppPromoteToLeader = _reflection.GeneratedProtocolMessageType('AppPromoteToLeader', (_message.Message,), {
  'DESCRIPTOR' : _APPPROMOTETOLEADER,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppPromoteToLeader)
  })
_sym_db.RegisterMessage(AppPromoteToLeader)

AppResponse = _reflection.GeneratedProtocolMessageType('AppResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPRESPONSE,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppResponse)
  })
_sym_db.RegisterMessage(AppResponse)

AppBroadcast = _reflection.GeneratedProtocolMessageType('AppBroadcast', (_message.Message,), {
  'DESCRIPTOR' : _APPBROADCAST,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppBroadcast)
  })
_sym_db.RegisterMessage(AppBroadcast)

AppEmpty = _reflection.GeneratedProtocolMessageType('AppEmpty', (_message.Message,), {
  'DESCRIPTOR' : _APPEMPTY,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppEmpty)
  })
_sym_db.RegisterMessage(AppEmpty)

AppSuccess = _reflection.GeneratedProtocolMessageType('AppSuccess', (_message.Message,), {
  'DESCRIPTOR' : _APPSUCCESS,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppSuccess)
  })
_sym_db.RegisterMessage(AppSuccess)

AppError = _reflection.GeneratedProtocolMessageType('AppError', (_message.Message,), {
  'DESCRIPTOR' : _APPERROR,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppError)
  })
_sym_db.RegisterMessage(AppError)

AppInfo = _reflection.GeneratedProtocolMessageType('AppInfo', (_message.Message,), {
  'DESCRIPTOR' : _APPINFO,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppInfo)
  })
_sym_db.RegisterMessage(AppInfo)

AppTime = _reflection.GeneratedProtocolMessageType('AppTime', (_message.Message,), {
  'DESCRIPTOR' : _APPTIME,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppTime)
  })
_sym_db.RegisterMessage(AppTime)

AppMap = _reflection.GeneratedProtocolMessageType('AppMap', (_message.Message,), {

  'Monument' : _reflection.GeneratedProtocolMessageType('Monument', (_message.Message,), {
    'DESCRIPTOR' : _APPMAP_MONUMENT,
    '__module__' : 'rustplus_pb2'
    # @@protoc_insertion_point(class_scope:rustplus.AppMap.Monument)
    })
  ,
  'DESCRIPTOR' : _APPMAP,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppMap)
  })
_sym_db.RegisterMessage(AppMap)
_sym_db.RegisterMessage(AppMap.Monument)

AppTeamInfo = _reflection.GeneratedProtocolMessageType('AppTeamInfo', (_message.Message,), {

  'Member' : _reflection.GeneratedProtocolMessageType('Member', (_message.Message,), {
    'DESCRIPTOR' : _APPTEAMINFO_MEMBER,
    '__module__' : 'rustplus_pb2'
    # @@protoc_insertion_point(class_scope:rustplus.AppTeamInfo.Member)
    })
  ,

  'Note' : _reflection.GeneratedProtocolMessageType('Note', (_message.Message,), {
    'DESCRIPTOR' : _APPTEAMINFO_NOTE,
    '__module__' : 'rustplus_pb2'
    # @@protoc_insertion_point(class_scope:rustplus.AppTeamInfo.Note)
    })
  ,
  'DESCRIPTOR' : _APPTEAMINFO,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppTeamInfo)
  })
_sym_db.RegisterMessage(AppTeamInfo)
_sym_db.RegisterMessage(AppTeamInfo.Member)
_sym_db.RegisterMessage(AppTeamInfo.Note)

AppTeamChat = _reflection.GeneratedProtocolMessageType('AppTeamChat', (_message.Message,), {
  'DESCRIPTOR' : _APPTEAMCHAT,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppTeamChat)
  })
_sym_db.RegisterMessage(AppTeamChat)

AppChatMessage = _reflection.GeneratedProtocolMessageType('AppChatMessage', (_message.Message,), {
  'DESCRIPTOR' : _APPCHATMESSAGE,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppChatMessage)
  })
_sym_db.RegisterMessage(AppChatMessage)

AppEntityInfo = _reflection.GeneratedProtocolMessageType('AppEntityInfo', (_message.Message,), {
  'DESCRIPTOR' : _APPENTITYINFO,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppEntityInfo)
  })
_sym_db.RegisterMessage(AppEntityInfo)

AppEntityPayload = _reflection.GeneratedProtocolMessageType('AppEntityPayload', (_message.Message,), {

  'Item' : _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
    'DESCRIPTOR' : _APPENTITYPAYLOAD_ITEM,
    '__module__' : 'rustplus_pb2'
    # @@protoc_insertion_point(class_scope:rustplus.AppEntityPayload.Item)
    })
  ,
  'DESCRIPTOR' : _APPENTITYPAYLOAD,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppEntityPayload)
  })
_sym_db.RegisterMessage(AppEntityPayload)
_sym_db.RegisterMessage(AppEntityPayload.Item)

AppFlag = _reflection.GeneratedProtocolMessageType('AppFlag', (_message.Message,), {
  'DESCRIPTOR' : _APPFLAG,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppFlag)
  })
_sym_db.RegisterMessage(AppFlag)

AppMapMarkers = _reflection.GeneratedProtocolMessageType('AppMapMarkers', (_message.Message,), {
  'DESCRIPTOR' : _APPMAPMARKERS,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppMapMarkers)
  })
_sym_db.RegisterMessage(AppMapMarkers)

Vector4 = _reflection.GeneratedProtocolMessageType('Vector4', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR4,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.Vector4)
  })
_sym_db.RegisterMessage(Vector4)

AppMarker = _reflection.GeneratedProtocolMessageType('AppMarker', (_message.Message,), {

  'SellOrder' : _reflection.GeneratedProtocolMessageType('SellOrder', (_message.Message,), {
    'DESCRIPTOR' : _APPMARKER_SELLORDER,
    '__module__' : 'rustplus_pb2'
    # @@protoc_insertion_point(class_scope:rustplus.AppMarker.SellOrder)
    })
  ,
  'DESCRIPTOR' : _APPMARKER,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppMarker)
  })
_sym_db.RegisterMessage(AppMarker)
_sym_db.RegisterMessage(AppMarker.SellOrder)

AppCameraFrame = _reflection.GeneratedProtocolMessageType('AppCameraFrame', (_message.Message,), {
  'DESCRIPTOR' : _APPCAMERAFRAME,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppCameraFrame)
  })
_sym_db.RegisterMessage(AppCameraFrame)

AppTeamChanged = _reflection.GeneratedProtocolMessageType('AppTeamChanged', (_message.Message,), {
  'DESCRIPTOR' : _APPTEAMCHANGED,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppTeamChanged)
  })
_sym_db.RegisterMessage(AppTeamChanged)

AppTeamMessage = _reflection.GeneratedProtocolMessageType('AppTeamMessage', (_message.Message,), {
  'DESCRIPTOR' : _APPTEAMMESSAGE,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppTeamMessage)
  })
_sym_db.RegisterMessage(AppTeamMessage)

AppEntityChanged = _reflection.GeneratedProtocolMessageType('AppEntityChanged', (_message.Message,), {
  'DESCRIPTOR' : _APPENTITYCHANGED,
  '__module__' : 'rustplus_pb2'
  # @@protoc_insertion_point(class_scope:rustplus.AppEntityChanged)
  })
_sym_db.RegisterMessage(AppEntityChanged)


# @@protoc_insertion_point(module_scope)
