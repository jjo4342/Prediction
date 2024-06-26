# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from msgs/object_msg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class object_msg(genpy.Message):
  _md5sum = "8dcaecefb527431a134307cc7d2d00d0"
  _type = "msgs/object_msg"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """int32 id
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
  __slots__ = ['id','mode','status','x','y','vx','vy','ax','ay','size_x','size_y','orientation']
  _slot_types = ['int32','int32','uint8','float64','float64','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,mode,status,x,y,vx,vy,ax,ay,size_x,size_y,orientation

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(object_msg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.mode is None:
        self.mode = 0
      if self.status is None:
        self.status = 0
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.vx is None:
        self.vx = 0.
      if self.vy is None:
        self.vy = 0.
      if self.ax is None:
        self.ax = 0.
      if self.ay is None:
        self.ay = 0.
      if self.size_x is None:
        self.size_x = 0.
      if self.size_y is None:
        self.size_y = 0.
      if self.orientation is None:
        self.orientation = 0.
    else:
      self.id = 0
      self.mode = 0
      self.status = 0
      self.x = 0.
      self.y = 0.
      self.vx = 0.
      self.vy = 0.
      self.ax = 0.
      self.ay = 0.
      self.size_x = 0.
      self.size_y = 0.
      self.orientation = 0.

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
      _x = self
      buff.write(_get_struct_2iB9d().pack(_x.id, _x.mode, _x.status, _x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.size_x, _x.size_y, _x.orientation))
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
      end = 0
      _x = self
      start = end
      end += 81
      (_x.id, _x.mode, _x.status, _x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.size_x, _x.size_y, _x.orientation,) = _get_struct_2iB9d().unpack(str[start:end])
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
      _x = self
      buff.write(_get_struct_2iB9d().pack(_x.id, _x.mode, _x.status, _x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.size_x, _x.size_y, _x.orientation))
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
      end = 0
      _x = self
      start = end
      end += 81
      (_x.id, _x.mode, _x.status, _x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.size_x, _x.size_y, _x.orientation,) = _get_struct_2iB9d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2iB9d = None
def _get_struct_2iB9d():
    global _struct_2iB9d
    if _struct_2iB9d is None:
        _struct_2iB9d = struct.Struct("<2iB9d")
    return _struct_2iB9d
