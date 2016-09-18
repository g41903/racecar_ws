# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from visual_servoing/CameraObject.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class CameraObject(genpy.Message):
  _md5sum = "d478c17254577f2d7871f7b466c8761a"
  _type = "visual_servoing/CameraObject"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string label
geometry_msgs/Point center  # in pixels, from center (haha, maybe not really)
geometry_msgs/Vector3 size  # in pixels

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['label','center','size']
  _slot_types = ['string','geometry_msgs/Point','geometry_msgs/Vector3']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       label,center,size

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CameraObject, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.label is None:
        self.label = ''
      if self.center is None:
        self.center = geometry_msgs.msg.Point()
      if self.size is None:
        self.size = geometry_msgs.msg.Vector3()
    else:
      self.label = ''
      self.center = geometry_msgs.msg.Point()
      self.size = geometry_msgs.msg.Vector3()

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
      _x = self.label
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6d.pack(_x.center.x, _x.center.y, _x.center.z, _x.size.x, _x.size.y, _x.size.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.center is None:
        self.center = geometry_msgs.msg.Point()
      if self.size is None:
        self.size = geometry_msgs.msg.Vector3()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.label = str[start:end].decode('utf-8')
      else:
        self.label = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.center.x, _x.center.y, _x.center.z, _x.size.x, _x.size.y, _x.size.z,) = _struct_6d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.label
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6d.pack(_x.center.x, _x.center.y, _x.center.z, _x.size.x, _x.size.y, _x.size.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.center is None:
        self.center = geometry_msgs.msg.Point()
      if self.size is None:
        self.size = geometry_msgs.msg.Vector3()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.label = str[start:end].decode('utf-8')
      else:
        self.label = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.center.x, _x.center.y, _x.center.z, _x.size.x, _x.size.y, _x.size.z,) = _struct_6d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_6d = struct.Struct("<6d")
