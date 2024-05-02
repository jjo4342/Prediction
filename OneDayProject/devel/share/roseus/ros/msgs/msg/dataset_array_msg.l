;; Auto-generated. Do not edit!


(when (boundp 'msgs::dataset_array_msg)
  (if (not (find-package "MSGS"))
    (make-package "MSGS"))
  (shadow 'dataset_array_msg (find-package "MSGS")))
(unless (find-package "MSGS::DATASET_ARRAY_MSG")
  (make-package "MSGS::DATASET_ARRAY_MSG"))

(in-package "ROS")
;;//! \htmlinclude dataset_array_msg.msg.html


(defclass msgs::dataset_array_msg
  :super ros::object
  :slots (_data _time ))

(defmethod msgs::dataset_array_msg
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
    ;; msgs/dataset_msg[] _data
    (apply #'+ (send-all _data :serialization-length)) 4
    ;; time _time
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; msgs/dataset_msg[] _data
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
   ;; msgs/dataset_msg[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (let (r) (dotimes (i n) (push (instance msgs::dataset_msg :init) r)) r))
     (dolist (elem- _data)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; time _time
     (send _time :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _time :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get msgs::dataset_array_msg :md5sum-) "bbbdf2033e5021290631028b34c0b877")
(setf (get msgs::dataset_array_msg :datatype-) "msgs/dataset_array_msg")
(setf (get msgs::dataset_array_msg :definition-)
      "dataset_msg[] data
time time

================================================================================
MSG: msgs/dataset_msg
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

")



(provide :msgs/dataset_array_msg "bbbdf2033e5021290631028b34c0b877")


