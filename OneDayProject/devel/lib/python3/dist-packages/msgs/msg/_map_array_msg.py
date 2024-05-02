# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from msgs/map_array_msg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import msgs.msg

class map_array_msg(genpy.Message):
  _md5sum = "b1600958de547559bb606d694ebf501a"
  _type = "msgs/map_array_msg"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """map_msg[] data
time time


================================================================================
MSG: msgs/map_msg
int16 path_id
int16 left_path_id
int16 right_path_id
int16[] succesors
int16[] predecessors

point_msg[] center


================================================================================
MSG: msgs/point_msg
float64 x
float64 y
float64 s
float64 d

"""
  __slots__ = ['data','time']
  _slot_types = ['msgs/map_msg[]','time']

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
      super(map_array_msg, self).__init__(*args, **kwds)
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
        buff.write(_get_struct_3h().pack(_x.path_id, _x.left_path_id, _x.right_path_id))
        length = len(val1.succesors)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(struct.Struct(pattern).pack(*val1.succesors))
        length = len(val1.predecessors)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(struct.Struct(pattern).pack(*val1.predecessors))
        length = len(val1.center)
        buff.write(_struct_I.pack(length))
        for val2 in val1.center:
          _x = val2
          buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.s, _x.d))
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
        val1 = msgs.msg.map_msg()
        _x = val1
        start = end
        end += 6
        (_x.path_id, _x.left_path_id, _x.right_path_id,) = _get_struct_3h().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sh'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.succesors = s.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sh'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.predecessors = s.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.center = []
        for i in range(0, length):
          val2 = msgs.msg.point_msg()
          _x = val2
          start = end
          end += 32
          (_x.x, _x.y, _x.s, _x.d,) = _get_struct_4d().unpack(str[start:end])
          val1.center.append(val2)
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
        buff.write(_get_struct_3h().pack(_x.path_id, _x.left_path_id, _x.right_path_id))
        length = len(val1.succesors)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(val1.succesors.tostring())
        length = len(val1.predecessors)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(val1.predecessors.tostring())
        length = len(val1.center)
        buff.write(_struct_I.pack(length))
        for val2 in val1.center:
          _x = val2
          buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.s, _x.d))
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
        val1 = msgs.msg.map_msg()
        _x = val1
        start = end
        end += 6
        (_x.path_id, _x.left_path_id, _x.right_path_id,) = _get_struct_3h().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sh'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.succesors = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sh'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.predecessors = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.center = []
        for i in range(0, length):
          val2 = msgs.msg.point_msg()
          _x = val2
          start = end
          end += 32
          (_x.x, _x.y, _x.s, _x.d,) = _get_struct_4d().unpack(str[start:end])
          val1.center.append(val2)
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
_struct_3h = None
def _get_struct_3h():
    global _struct_3h
    if _struct_3h is None:
        _struct_3h = struct.Struct("<3h")
    return _struct_3h
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
