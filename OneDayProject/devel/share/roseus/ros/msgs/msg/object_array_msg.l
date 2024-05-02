;; Auto-generated. Do not edit!


(when (boundp 'msgs::object_array_msg)
  (if (not (find-package "MSGS"))
    (make-package "MSGS"))
  (shadow 'object_array_msg (find-package "MSGS")))
(unless (find-package "MSGS::OBJECT_ARRAY_MSG")
  (make-package "MSGS::OBJECT_ARRAY_MSG"))

(in-package "ROS")
;;//! \htmlinclude object_array_msg.msg.html


(defclass msgs::object_array_msg
  :super ros::object
  :slots (_data _time ))

(defmethod msgs::object_array_msg
  (:init
   (&key
    ((:data __data) ())
    ((:time __time) (instance ros::time :init))
    )
   (send-super :init)
   (setq _data __data)
   (setq _time __time)
   self)
  (:data
   (&rest __data)
   (if (keywordp (car __data))
       (send* _data __data)
     (progn
       (if __data (setq _data (car __data)))
       _data)))
  (:time
   (&optional __time)
   (if __time (setq _time __time)) _time)
  (:serialization-length
   ()
   (+
    ;; msgs/object_msg[] _data
    (apply #'+ (send-all _data :serialization-length)) 4
    ;; time _time
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; msgs/object_msg[] _data
     (write-long (length _data) s)
     (dolist (elem _data)
       (send elem :serialize s)
       )
     ;; time _time
       (write-long (send _time :sec) s) (write-long (send _time :nsec) s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; msgs/object_msg[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (let (r) (dotimes (i n) (push (instance msgs::object_msg :init) r)) r))
     (dolist (elem- _data)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; time _time
     (send _time :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _time :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get msgs::object_array_msg :md5sum-) "846cc955642ddfe98e7a669371b51902")
(setf (get msgs::object_array_msg :datatype-) "msgs/object_array_msg")
(setf (get msgs::object_array_msg :definition-)
      "object_msg[] data
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

")



(provide :msgs/object_array_msg "846cc955642ddfe98e7a669371b51902")


