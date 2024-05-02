;; Auto-generated. Do not edit!


(when (boundp 'msgs::point_msg)
  (if (not (find-package "MSGS"))
    (make-package "MSGS"))
  (shadow 'point_msg (find-package "MSGS")))
(unless (find-package "MSGS::POINT_MSG")
  (make-package "MSGS::POINT_MSG"))

(in-package "ROS")
;;//! \htmlinclude point_msg.msg.html


(defclass msgs::point_msg
  :super ros::object
  :slots (_x _y _s _d ))

(defmethod msgs::point_msg
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:s __s) 0.0)
    ((:d __d) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _s (float __s))
   (setq _d (float __d))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:s
   (&optional __s)
   (if __s (setq _s __s)) _s)
  (:d
   (&optional __d)
   (if __d (setq _d __d)) _d)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _s
    8
    ;; float64 _d
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _s
       (sys::poke _s (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _d
       (sys::poke _d (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _s
     (setq _s (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _d
     (setq _d (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get msgs::point_msg :md5sum-) "90302bac96ad7533542a9dac3cf8ba5f")
(setf (get msgs::point_msg :datatype-) "msgs/point_msg")
(setf (get msgs::point_msg :definition-)
      "float64 x
float64 y
float64 s
float64 d


")



(provide :msgs/point_msg "90302bac96ad7533542a9dac3cf8ba5f")


