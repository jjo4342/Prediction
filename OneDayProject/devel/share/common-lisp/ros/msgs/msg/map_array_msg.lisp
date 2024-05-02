; Auto-generated. Do not edit!


(cl:in-package msgs-msg)


;//! \htmlinclude map_array_msg.msg.html

(cl:defclass <map_array_msg> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type (cl:vector msgs-msg:map_msg)
   :initform (cl:make-array 0 :element-type 'msgs-msg:map_msg :initial-element (cl:make-instance 'msgs-msg:map_msg)))
   (time
    :reader time
    :initarg :time
    :type cl:real
    :initform 0))
)

(cl:defclass map_array_msg (<map_array_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <map_array_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'map_array_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name msgs-msg:<map_array_msg> is deprecated: use msgs-msg:map_array_msg instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <map_array_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msgs-msg:data-val is deprecated.  Use msgs-msg:data instead.")
  (data m))

(cl:ensure-generic-function 'time-val :lambda-list '(m))
(cl:defmethod time-val ((m <map_array_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msgs-msg:time-val is deprecated.  Use msgs-msg:time instead.")
  (time m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <map_array_msg>) ostream)
  "Serializes a message object of type '<map_array_msg>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'data))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'time)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'time) (cl:floor (cl:slot-value msg 'time)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <map_array_msg>) istream)
  "Deserializes a message object of type '<map_array_msg>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'msgs-msg:map_msg))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'time) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<map_array_msg>)))
  "Returns string type for a message object of type '<map_array_msg>"
  "msgs/map_array_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'map_array_msg)))
  "Returns string type for a message object of type 'map_array_msg"
  "msgs/map_array_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<map_array_msg>)))
  "Returns md5sum for a message object of type '<map_array_msg>"
  "b1600958de547559bb606d694ebf501a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'map_array_msg)))
  "Returns md5sum for a message object of type 'map_array_msg"
  "b1600958de547559bb606d694ebf501a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<map_array_msg>)))
  "Returns full string definition for message of type '<map_array_msg>"
  (cl:format cl:nil "map_msg[] data~%time time~%~%~%================================================================================~%MSG: msgs/map_msg~%int16 path_id~%int16 left_path_id~%int16 right_path_id~%int16[] succesors~%int16[] predecessors~%~%point_msg[] center~%~%~%================================================================================~%MSG: msgs/point_msg~%float64 x~%float64 y~%float64 s~%float64 d~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'map_array_msg)))
  "Returns full string definition for message of type 'map_array_msg"
  (cl:format cl:nil "map_msg[] data~%time time~%~%~%================================================================================~%MSG: msgs/map_msg~%int16 path_id~%int16 left_path_id~%int16 right_path_id~%int16[] succesors~%int16[] predecessors~%~%point_msg[] center~%~%~%================================================================================~%MSG: msgs/point_msg~%float64 x~%float64 y~%float64 s~%float64 d~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <map_array_msg>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <map_array_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'map_array_msg
    (cl:cons ':data (data msg))
    (cl:cons ':time (time msg))
))
