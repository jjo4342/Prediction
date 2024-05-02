; Auto-generated. Do not edit!


(cl:in-package msgs-msg)


;//! \htmlinclude map_msg.msg.html

(cl:defclass <map_msg> (roslisp-msg-protocol:ros-message)
  ((path_id
    :reader path_id
    :initarg :path_id
    :type cl:fixnum
    :initform 0)
   (left_path_id
    :reader left_path_id
    :initarg :left_path_id
    :type cl:fixnum
    :initform 0)
   (right_path_id
    :reader right_path_id
    :initarg :right_path_id
    :type cl:fixnum
    :initform 0)
   (succesors
    :reader succesors
    :initarg :succesors
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0))
   (predecessors
    :reader predecessors
    :initarg :predecessors
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0))
   (center
    :reader center
    :initarg :center
    :type (cl:vector msgs-msg:point_msg)
   :initform (cl:make-array 0 :element-type 'msgs-msg:point_msg :initial-element (cl:make-instance 'msgs-msg:point_msg))))
)

(cl:defclass map_msg (<map_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <map_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'map_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name msgs-msg:<map_msg> is deprecated: use msgs-msg:map_msg instead.")))

(cl:ensure-generic-function 'path_id-val :lambda-list '(m))
(cl:defmethod path_id-val ((m <map_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msgs-msg:path_id-val is deprecated.  Use msgs-msg:path_id instead.")
  (path_id m))

(cl:ensure-generic-function 'left_path_id-val :lambda-list '(m))
(cl:defmethod left_path_id-val ((m <map_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msgs-msg:left_path_id-val is deprecated.  Use msgs-msg:left_path_id instead.")
  (left_path_id m))

(cl:ensure-generic-function 'right_path_id-val :lambda-list '(m))
(cl:defmethod right_path_id-val ((m <map_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msgs-msg:right_path_id-val is deprecated.  Use msgs-msg:right_path_id instead.")
  (right_path_id m))

(cl:ensure-generic-function 'succesors-val :lambda-list '(m))
(cl:defmethod succesors-val ((m <map_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msgs-msg:succesors-val is deprecated.  Use msgs-msg:succesors instead.")
  (succesors m))

(cl:ensure-generic-function 'predecessors-val :lambda-list '(m))
(cl:defmethod predecessors-val ((m <map_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msgs-msg:predecessors-val is deprecated.  Use msgs-msg:predecessors instead.")
  (predecessors m))

(cl:ensure-generic-function 'center-val :lambda-list '(m))
(cl:defmethod center-val ((m <map_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader msgs-msg:center-val is deprecated.  Use msgs-msg:center instead.")
  (center m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <map_msg>) ostream)
  "Serializes a message object of type '<map_msg>"
  (cl:let* ((signed (cl:slot-value msg 'path_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'left_path_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'right_path_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'succesors))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'succesors))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'predecessors))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'predecessors))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'center))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'center))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <map_msg>) istream)
  "Deserializes a message object of type '<map_msg>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'path_id) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'left_path_id) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'right_path_id) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'succesors) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'succesors)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'predecessors) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'predecessors)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'center) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'center)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'msgs-msg:point_msg))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<map_msg>)))
  "Returns string type for a message object of type '<map_msg>"
  "msgs/map_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'map_msg)))
  "Returns string type for a message object of type 'map_msg"
  "msgs/map_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<map_msg>)))
  "Returns md5sum for a message object of type '<map_msg>"
  "74bec9aa085584f3c79b706501e2c126")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'map_msg)))
  "Returns md5sum for a message object of type 'map_msg"
  "74bec9aa085584f3c79b706501e2c126")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<map_msg>)))
  "Returns full string definition for message of type '<map_msg>"
  (cl:format cl:nil "int16 path_id~%int16 left_path_id~%int16 right_path_id~%int16[] succesors~%int16[] predecessors~%~%point_msg[] center~%~%~%================================================================================~%MSG: msgs/point_msg~%float64 x~%float64 y~%float64 s~%float64 d~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'map_msg)))
  "Returns full string definition for message of type 'map_msg"
  (cl:format cl:nil "int16 path_id~%int16 left_path_id~%int16 right_path_id~%int16[] succesors~%int16[] predecessors~%~%point_msg[] center~%~%~%================================================================================~%MSG: msgs/point_msg~%float64 x~%float64 y~%float64 s~%float64 d~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <map_msg>))
  (cl:+ 0
     2
     2
     2
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'succesors) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'predecessors) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'center) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <map_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'map_msg
    (cl:cons ':path_id (path_id msg))
    (cl:cons ':left_path_id (left_path_id msg))
    (cl:cons ':right_path_id (right_path_id msg))
    (cl:cons ':succesors (succesors msg))
    (cl:cons ':predecessors (predecessors msg))
    (cl:cons ':center (center msg))
))
