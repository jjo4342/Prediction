// Auto-generated. Do not edit!

// (in-package msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let point_msg = require('./point_msg.js');

//-----------------------------------------------------------

class map_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.path_id = null;
      this.left_path_id = null;
      this.right_path_id = null;
      this.succesors = null;
      this.predecessors = null;
      this.center = null;
    }
    else {
      if (initObj.hasOwnProperty('path_id')) {
        this.path_id = initObj.path_id
      }
      else {
        this.path_id = 0;
      }
      if (initObj.hasOwnProperty('left_path_id')) {
        this.left_path_id = initObj.left_path_id
      }
      else {
        this.left_path_id = 0;
      }
      if (initObj.hasOwnProperty('right_path_id')) {
        this.right_path_id = initObj.right_path_id
      }
      else {
        this.right_path_id = 0;
      }
      if (initObj.hasOwnProperty('succesors')) {
        this.succesors = initObj.succesors
      }
      else {
        this.succesors = [];
      }
      if (initObj.hasOwnProperty('predecessors')) {
        this.predecessors = initObj.predecessors
      }
      else {
        this.predecessors = [];
      }
      if (initObj.hasOwnProperty('center')) {
        this.center = initObj.center
      }
      else {
        this.center = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type map_msg
    // Serialize message field [path_id]
    bufferOffset = _serializer.int16(obj.path_id, buffer, bufferOffset);
    // Serialize message field [left_path_id]
    bufferOffset = _serializer.int16(obj.left_path_id, buffer, bufferOffset);
    // Serialize message field [right_path_id]
    bufferOffset = _serializer.int16(obj.right_path_id, buffer, bufferOffset);
    // Serialize message field [succesors]
    bufferOffset = _arraySerializer.int16(obj.succesors, buffer, bufferOffset, null);
    // Serialize message field [predecessors]
    bufferOffset = _arraySerializer.int16(obj.predecessors, buffer, bufferOffset, null);
    // Serialize message field [center]
    // Serialize the length for message field [center]
    bufferOffset = _serializer.uint32(obj.center.length, buffer, bufferOffset);
    obj.center.forEach((val) => {
      bufferOffset = point_msg.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type map_msg
    let len;
    let data = new map_msg(null);
    // Deserialize message field [path_id]
    data.path_id = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [left_path_id]
    data.left_path_id = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [right_path_id]
    data.right_path_id = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [succesors]
    data.succesors = _arrayDeserializer.int16(buffer, bufferOffset, null)
    // Deserialize message field [predecessors]
    data.predecessors = _arrayDeserializer.int16(buffer, bufferOffset, null)
    // Deserialize message field [center]
    // Deserialize array length for message field [center]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.center = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.center[i] = point_msg.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 2 * object.succesors.length;
    length += 2 * object.predecessors.length;
    length += 32 * object.center.length;
    return length + 18;
  }

  static datatype() {
    // Returns string type for a message object
    return 'msgs/map_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '74bec9aa085584f3c79b706501e2c126';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new map_msg(null);
    if (msg.path_id !== undefined) {
      resolved.path_id = msg.path_id;
    }
    else {
      resolved.path_id = 0
    }

    if (msg.left_path_id !== undefined) {
      resolved.left_path_id = msg.left_path_id;
    }
    else {
      resolved.left_path_id = 0
    }

    if (msg.right_path_id !== undefined) {
      resolved.right_path_id = msg.right_path_id;
    }
    else {
      resolved.right_path_id = 0
    }

    if (msg.succesors !== undefined) {
      resolved.succesors = msg.succesors;
    }
    else {
      resolved.succesors = []
    }

    if (msg.predecessors !== undefined) {
      resolved.predecessors = msg.predecessors;
    }
    else {
      resolved.predecessors = []
    }

    if (msg.center !== undefined) {
      resolved.center = new Array(msg.center.length);
      for (let i = 0; i < resolved.center.length; ++i) {
        resolved.center[i] = point_msg.Resolve(msg.center[i]);
      }
    }
    else {
      resolved.center = []
    }

    return resolved;
    }
};

module.exports = map_msg;
