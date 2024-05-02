# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from msgs/object_array_msg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import msgs.msg

class object_array_msg(genpy.Message):
  _md5sum = "846cc955642ddfe98e7a669371b51902"
  _type = "msgs/object_array_msg"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """object_msg[] data
time time

================================================================================
MSG: msgs/object_msg
int32 id
int32 mode
uint8 status
float64 x
float64 y
float64 vx
float64 vy
float64 ax
float64 ay
float64 size_x
float64 size_y
float64 orientation
"""
  __slots__ = ['data','time']
  _slot_types = ['msgs/object_msg[]','time']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       data,time

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(object_array_msg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.data is None:
        self.data = []
      if self.time is None:
        self.time = genpy.Time()
    else:
      self.data = []
      self.time = genpy.Time()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data:
        _x = val1
        buff.write(_get_struct_2iB9d().pack(_x.id, _x.mode, _x.status, _x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.size_x, _x.size_y, _x.orientation))
      _x = self
      buff.write(_get_struct_2I().pack(_x.time.secs, _x.time.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.data is None:
        self.data = None
      if self.time is None:
        self.time = genpy.Time()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data = []
      for i in range(0, length):
        val1 = msgs.msg.object_msg()
        _x = val1
        start = end
        end += 81
        (_x.id, _x.mode, _x.status, _x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.size_x, _x.size_y, _x.orientation,) = _get_struct_2iB9d().unpack(str[start:end])
        self.data.append(val1)
      _x = self
      start = end
      end += 8
      (_x.time.secs, _x.time.nsecs,) = _get_struct_2I().unpack(str[start:end])
      self.time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data:
        _x = val1
        buff.write(_get_struct_2iB9d().pack(_x.id, _x.mode, _x.status, _x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.size_x, _x.size_y, _x.orientation))
      _x = self
      buff.write(_get_struct_2I().pack(_x.time.secs, _x.time.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.data is None:
        self.data = None
      if self.time is None:
        self.time = genpy.Time()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data = []
      for i in range(0, length):
        val1 = msgs.msg.object_msg()
        _x = val1
        start = end
        end += 81
        (_x.id, _x.mode, _x.status, _x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.size_x, _x.size_y, _x.orientation,) = _get_struct_2iB9d().unpack(str[start:end])
        self.data.append(val1)
      _x = self
      start = end
      end += 8
      (_x.time.secs, _x.time.nsecs,) = _get_struct_2I().unpack(str[start:end])
      self.time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_2iB9d = None
def _get_struct_2iB9d():
    global _struct_2iB9d
    if _struct_2iB9d is None:
        _struct_2iB9d = struct.Struct("<2iB9d")
    return _struct_2iB9d
