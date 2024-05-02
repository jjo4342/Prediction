// Auto-generated. Do not edit!

// (in-package msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class dataset_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.id = null;
      this.lane_id = null;
      this.length = null;
      this.width = null;
      this.x = null;
      this.y = null;
      this.yaw = null;
      this.vx = null;
      this.vy = null;
      this.s = null;
      this.d = null;
      this.mask = null;
      this.mode = null;
    }
    else {
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = 0;
      }
      if (initObj.hasOwnProperty('lane_id')) {
        this.lane_id = initObj.lane_id
      }
      else {
        this.lane_id = 0;
      }
      if (initObj.hasOwnProperty('length')) {
        this.length = initObj.length
      }
      else {
        this.length = 0.0;
      }
      if (initObj.hasOwnProperty('width')) {
        this.width = initObj.width
      }
      else {
        this.width = 0.0;
      }
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = [];
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = [];
      }
      if (initObj.hasOwnProperty('yaw')) {
        this.yaw = initObj.yaw
      }
      else {
        this.yaw = [];
      }
      if (initObj.hasOwnProperty('vx')) {
        this.vx = initObj.vx
      }
      else {
        this.vx = [];
      }
      if (initObj.hasOwnProperty('vy')) {
        this.vy = initObj.vy
      }
      else {
        this.vy = [];
      }
      if (initObj.hasOwnProperty('s')) {
        this.s = initObj.s
      }
      else {
        this.s = [];
      }
      if (initObj.hasOwnProperty('d')) {
        this.d = initObj.d
      }
      else {
        this.d = [];
      }
      if (initObj.hasOwnProperty('mask')) {
        this.mask = initObj.mask
      }
      else {
        this.mask = [];
      }
      if (initObj.hasOwnProperty('mode')) {
        this.mode = initObj.mode
      }
      else {
        this.mode = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type dataset_msg
    // Serialize message field [id]
    bufferOffset = _serializer.int32(obj.id, buffer, bufferOffset);
    // Serialize message field [lane_id]
    bufferOffset = _serializer.int32(obj.lane_id, buffer, bufferOffset);
    // Serialize message field [length]
    bufferOffset = _serializer.float32(obj.length, buffer, bufferOffset);
    // Serialize message field [width]
    bufferOffset = _serializer.float32(obj.width, buffer, bufferOffset);
    // Serialize message field [x]
    bufferOffset = _arraySerializer.float64(obj.x, buffer, bufferOffset, null);
    // Serialize message field [y]
    bufferOffset = _arraySerializer.float64(obj.y, buffer, bufferOffset, null);
    // Serialize message field [yaw]
    bufferOffset = _arraySerializer.float64(obj.yaw, buffer, bufferOffset, null);
    // Serialize message field [vx]
    bufferOffset = _arraySerializer.float64(obj.vx, buffer, bufferOffset, null);
    // Serialize message field [vy]
    bufferOffset = _arraySerializer.float64(obj.vy, buffer, bufferOffset, null);
    // Serialize message field [s]
    bufferOffset = _arraySerializer.float64(obj.s, buffer, bufferOffset, null);
    // Serialize message field [d]
    bufferOffset = _arraySerializer.float64(obj.d, buffer, bufferOffset, null);
    // Serialize message field [mask]
    bufferOffset = _arraySerializer.int32(obj.mask, buffer, bufferOffset, null);
    // Serialize message field [mode]
    bufferOffset = _serializer.int32(obj.mode, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type dataset_msg
    let len;
    let data = new dataset_msg(null);
    // Deserialize message field [id]
    data.id = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [lane_id]
    data.lane_id = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [length]
    data.length = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [width]
    data.width = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [x]
    data.x = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [y]
    data.y = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [yaw]
    data.yaw = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [vx]
    data.vx = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [vy]
    data.vy = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [s]
    data.s = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [d]
    data.d = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [mask]
    data.mask = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [mode]
    data.mode = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.x.length;
    length += 8 * object.y.length;
    length += 8 * object.yaw.length;
    length += 8 * object.vx.length;
    length += 8 * object.vy.length;
    length += 8 * object.s.length;
    length += 8 * object.d.length;
    length += 4 * object.mask.length;
    return length + 52;
  }

  static datatype() {
    // Returns string type for a message object
    return 'msgs/dataset_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'cc7ab277cce2b49147bf262deae10b1d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 id
    int32 lane_id
    float32 length
    float32 width
    float64[] x
    float64[] y
    float64[] yaw
    float64[] vx
    float64[] vy
    float64[] s
    float64[] d
    int32[] mask
    int32 mode
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new dataset_msg(null);
    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = 0
    }

    if (msg.lane_id !== undefined) {
      resolved.lane_id = msg.lane_id;
    }
    else {
      resolved.lane_id = 0
    }

    if (msg.length !== undefined) {
      resolved.length = msg.length;
    }
    else {
      resolved.length = 0.0
    }

    if (msg.width !== undefined) {
      resolved.width = msg.width;
    }
    else {
      resolved.width = 0.0
    }

    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = []
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = []
    }

    if (msg.yaw !== undefined) {
      resolved.yaw = msg.yaw;
    }
    else {
      resolved.yaw = []
    }

    if (msg.vx !== undefined) {
      resolved.vx = msg.vx;
    }
    else {
      resolved.vx = []
    }

    if (msg.vy !== undefined) {
      resolved.vy = msg.vy;
    }
    else {
      resolved.vy = []
    }

    if (msg.s !== undefined) {
      resolved.s = msg.s;
    }
    else {
      resolved.s = []
    }

    if (msg.d !== undefined) {
      resolved.d = msg.d;
    }
    else {
      resolved.d = []
    }

    if (msg.mask !== undefined) {
      resolved.mask = msg.mask;
    }
    else {
      resolved.mask = []
    }

    if (msg.mode !== undefined) {
      resolved.mode = msg.mode;
    }
    else {
      resolved.mode = 0
    }

    return resolved;
    }
};

module.exports = dataset_msg;
