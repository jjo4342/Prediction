// Auto-generated. Do not edit!

// (in-package msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let map_msg = require('./map_msg.js');

//-----------------------------------------------------------

class map_array_msg {
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
    // Serializes a message object of type map_array_msg
    // Serialize message field [data]
    // Serialize the length for message field [data]
    bufferOffset = _serializer.uint32(obj.data.length, buffer, bufferOffset);
    obj.data.forEach((val) => {
      bufferOffset = map_msg.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [time]
    bufferOffset = _serializer.time(obj.time, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type map_array_msg
    let len;
    let data = new map_array_msg(null);
    // Deserialize message field [data]
    // Deserialize array length for message field [data]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.data = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.data[i] = map_msg.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [time]
    data.time = _deserializer.time(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.data.forEach((val) => {
      length += map_msg.getMessageSize(val);
    });
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'msgs/map_array_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b1600958de547559bb606d694ebf501a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    map_msg[] data
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
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new map_array_msg(null);
    if (msg.data !== undefined) {
      resolved.data = new Array(msg.data.length);
      for (let i = 0; i < resolved.data.length; ++i) {
        resolved.data[i] = map_msg.Resolve(msg.data[i]);
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

module.exports = map_array_msg;
