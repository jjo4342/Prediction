;; Auto-generated. Do not edit!


(when (boundp 'msgs::map_array_msg)
  (if (not (find-package "MSGS"))
    (make-package "MSGS"))
  (shadow 'map_array_msg (find-package "MSGS")))
(unless (find-package "MSGS::MAP_ARRAY_MSG")
  (make-package "MSGS::MAP_ARRAY_MSG"))

(in-package "ROS")
;;//! \htmlinclude map_array_msg.msg.html


(defclass msgs::map_array_msg
  :super ros::object
  :slots (_data _time ))

(defmethod msgs::map_array_msg
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
    ;; msgs/map_msg[] _data
    (apply #'+ (send-all _data :serialization-length)) 4
    ;; time _time
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; msgs/map_msg[] _data
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
   ;; msgs/map_msg[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (let (r) (dotimes (i n) (push (instance msgs::map_msg :init) r)) r))
     (dolist (elem- _data)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; time _time
     (send _time :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _time :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get msgs::map_array_msg :md5sum-) "b1600958de547559bb606d694ebf501a")
(setf (get msgs::map_array_msg :datatype-) "msgs/map_array_msg")
(setf (get msgs::map_array_msg :definition-)
      "map_msg[] data
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


")



(provide :msgs/map_array_msg "b1600958de547559bb606d694ebf501a")


