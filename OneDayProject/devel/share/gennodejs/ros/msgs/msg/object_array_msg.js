// Auto-generated. Do not edit!

// (in-package msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let object_msg = require('./object_msg.js');

//-----------------------------------------------------------

class object_array_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.data = null;
      this.time = null;
    }
    else {
      if (initObj.hasOwnProperty('data')) {
        this.data = initObj.data
      }
      else {
        this.data = [];
      }
      if (initObj.hasOwnProperty('time')) {
        this.time = initObj.time
      }
      else {
        this.time = {secs: 0, nsecs: 0};
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type object_array_msg
    // Serialize message field [data]
    // Serialize the length for message field [data]
    bufferOffset = _serializer.uint32(obj.data.length, buffer, bufferOffset);
    obj.data.forEach((val) => {
      bufferOffset = object_msg.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [time]
    bufferOffset = _serializer.time(obj.time, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type object_array_msg
    let len;
    let data = new object_array_msg(null);
    // Deserialize message field [data]
    // Deserialize array length for message field [data]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.data = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.data[i] = object_msg.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [time]
    data.time = _deserializer.time(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 81 * object.data.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'msgs/object_array_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '846cc955642ddfe98e7a669371b51902';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    object_msg[] data
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new object_array_msg(null);
    if (msg.data !== undefined) {
      resolved.data = new Array(msg.data.length);
      for (let i = 0; i < resolved.data.length; ++i) {
        resolved.data[i] = object_msg.Resolve(msg.data[i]);
      }
    }
    else {
      resolved.data = []
    }

    if (msg.time !== undefined) {
      resolved.time = msg.time;
    }
    else {
      resolved.time = {secs: 0, nsecs: 0}
    }

    return resolved;
    }
};

module.exports = object_array_msg;
