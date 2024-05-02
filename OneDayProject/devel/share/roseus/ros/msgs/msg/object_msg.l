;; Auto-generated. Do not edit!


(when (boundp 'msgs::object_msg)
  (if (not (find-package "MSGS"))
    (make-package "MSGS"))
  (shadow 'object_msg (find-package "MSGS")))
(unless (find-package "MSGS::OBJECT_MSG")
  (make-package "MSGS::OBJECT_MSG"))

(in-package "ROS")
;;//! \htmlinclude object_msg.msg.html


(defclass msgs::object_msg
  :super ros::object
  :slots (_id _mode _status _x _y _vx _vy _ax _ay _size_x _size_y _orientation ))

(defmethod msgs::object_msg
  (:init
   (&key
    ((:id __id) 0)
    ((:mode __mode) 0)
    ((:status __status) 0)
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:vx __vx) 0.0)
    ((:vy __vy) 0.0)
    ((:ax __ax) 0.0)
    ((:ay __ay) 0.0)
    ((:size_x __size_x) 0.0)
    ((:size_y __size_y) 0.0)
    ((:orientation __orientation) 0.0)
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _mode (round __mode))
   (setq _status (round __status))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _vx (float __vx))
   (setq _vy (float __vy))
   (setq _ax (float __ax))
   (setq _ay (float __ay))
   (setq _size_x (float __size_x))
   (setq _size_y (float __size_y))
   (setq _orientation (float __orientation))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:mode
   (&optional __mode)
   (if __mode (setq _mode __mode)) _mode)
  (:status
   (&optional __status)
   (if __status (setq _status __status)) _status)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:vx
   (&optional __vx)
   (if __vx (setq _vx __vx)) _vx)
  (:vy
   (&optional __vy)
   (if __vy (setq _vy __vy)) _vy)
  (:ax
   (&optional __ax)
   (if __ax (setq _ax __ax)) _ax)
  (:ay
   (&optional __ay)
   (if __ay (setq _ay __ay)) _ay)
  (:size_x
   (&optional __size_x)
   (if __size_x (setq _size_x __size_x)) _size_x)
  (:size_y
   (&optional __size_y)
   (if __size_y (setq _size_y __size_y)) _size_y)
  (:orientation
   (&optional __orientation)
   (if __orientation (setq _orientation __orientation)) _orientation)
  (:serialization-length
   ()
   (+
    ;; int32 _id
    4
    ;; int32 _mode
    4
    ;; uint8 _status
    1
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _vx
    8
    ;; float64 _vy
    8
    ;; float64 _ax
    8
    ;; float64 _ay
    8
    ;; float64 _size_x
    8
    ;; float64 _size_y
    8
    ;; float64 _orientation
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _id
       (write-long _id s)
     ;; int32 _mode
       (write-long _mode s)
     ;; uint8 _status
       (write-byte _status s)
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vx
       (sys::poke _vx (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vy
       (sys::poke _vy (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ax
       (sys::poke _ax (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ay
       (sys::poke _ay (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _size_x
       (sys::poke _size_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _size_y
       (sys::poke _size_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _orientation
       (sys::poke _orientation (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _mode
     (setq _mode (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint8 _status
     (setq _status (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vx
     (setq _vx (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vy
     (setq _vy (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ax
     (setq _ax (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ay
     (setq _ay (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _size_x
     (setq _size_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _size_y
     (setq _size_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _orientation
     (setq _orientation (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get msgs::object_msg :md5sum-) "8dcaecefb527431a134307cc7d2d00d0")
(setf (get msgs::object_msg :datatype-) "msgs/object_msg")
(setf (get msgs::object_msg :definition-)
      "int32 id
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



(provide :msgs/object_msg "8dcaecefb527431a134307cc7d2d00d0")


