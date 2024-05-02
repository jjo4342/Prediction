;; Auto-generated. Do not edit!


(when (boundp 'msgs::dataset_msg)
  (if (not (find-package "MSGS"))
    (make-package "MSGS"))
  (shadow 'dataset_msg (find-package "MSGS")))
(unless (find-package "MSGS::DATASET_MSG")
  (make-package "MSGS::DATASET_MSG"))

(in-package "ROS")
;;//! \htmlinclude dataset_msg.msg.html


(defclass msgs::dataset_msg
  :super ros::object
  :slots (_id _lane_id _length _width _x _y _yaw _vx _vy _s _d _mask _mode ))

(defmethod msgs::dataset_msg
  (:init
   (&key
    ((:id __id) 0)
    ((:lane_id __lane_id) 0)
    ((:length __length) 0.0)
    ((:width __width) 0.0)
    ((:x __x) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:y __y) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:yaw __yaw) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:vx __vx) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:vy __vy) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:s __s) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:d __d) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:mask __mask) (make-array 0 :initial-element 0 :element-type :integer))
    ((:mode __mode) 0)
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _lane_id (round __lane_id))
   (setq _length (float __length))
   (setq _width (float __width))
   (setq _x __x)
   (setq _y __y)
   (setq _yaw __yaw)
   (setq _vx __vx)
   (setq _vy __vy)
   (setq _s __s)
   (setq _d __d)
   (setq _mask __mask)
   (setq _mode (round __mode))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:lane_id
   (&optional __lane_id)
   (if __lane_id (setq _lane_id __lane_id)) _lane_id)
  (:length
   (&optional __length)
   (if __length (setq _length __length)) _length)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:vx
   (&optional __vx)
   (if __vx (setq _vx __vx)) _vx)
  (:vy
   (&optional __vy)
   (if __vy (setq _vy __vy)) _vy)
  (:s
   (&optional __s)
   (if __s (setq _s __s)) _s)
  (:d
   (&optional __d)
   (if __d (setq _d __d)) _d)
  (:mask
   (&optional __mask)
   (if __mask (setq _mask __mask)) _mask)
  (:mode
   (&optional __mode)
   (if __mode (setq _mode __mode)) _mode)
  (:serialization-length
   ()
   (+
    ;; int32 _id
    4
    ;; int32 _lane_id
    4
    ;; float32 _length
    4
    ;; float32 _width
    4
    ;; float64[] _x
    (* 8    (length _x)) 4
    ;; float64[] _y
    (* 8    (length _y)) 4
    ;; float64[] _yaw
    (* 8    (length _yaw)) 4
    ;; float64[] _vx
    (* 8    (length _vx)) 4
    ;; float64[] _vy
    (* 8    (length _vy)) 4
    ;; float64[] _s
    (* 8    (length _s)) 4
    ;; float64[] _d
    (* 8    (length _d)) 4
    ;; int32[] _mask
    (* 4    (length _mask)) 4
    ;; int32 _mode
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _id
       (write-long _id s)
     ;; int32 _lane_id
       (write-long _lane_id s)
     ;; float32 _length
       (sys::poke _length (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _width
       (sys::poke _width (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float64[] _x
     (write-long (length _x) s)
     (dotimes (i (length _x))
       (sys::poke (elt _x i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _y
     (write-long (length _y) s)
     (dotimes (i (length _y))
       (sys::poke (elt _y i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _yaw
     (write-long (length _yaw) s)
     (dotimes (i (length _yaw))
       (sys::poke (elt _yaw i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _vx
     (write-long (length _vx) s)
     (dotimes (i (length _vx))
       (sys::poke (elt _vx i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _vy
     (write-long (length _vy) s)
     (dotimes (i (length _vy))
       (sys::poke (elt _vy i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _s
     (write-long (length _s) s)
     (dotimes (i (length _s))
       (sys::poke (elt _s i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _d
     (write-long (length _d) s)
     (dotimes (i (length _d))
       (sys::poke (elt _d i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; int32[] _mask
     (write-long (length _mask) s)
     (dotimes (i (length _mask))
       (write-long (elt _mask i) s)
       )
     ;; int32 _mode
       (write-long _mode s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _lane_id
     (setq _lane_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _length
     (setq _length (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _width
     (setq _width (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float64[] _x
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _x (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _x i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _y
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _y (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _y i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _yaw
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _yaw (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _yaw i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _vx
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _vx (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _vx i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _vy
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _vy (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _vy i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _s
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _s (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _s i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _d
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _d (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _d i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; int32[] _mask
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _mask (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _mask i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32 _mode
     (setq _mode (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get msgs::dataset_msg :md5sum-) "cc7ab277cce2b49147bf262deae10b1d")
(setf (get msgs::dataset_msg :datatype-) "msgs/dataset_msg")
(setf (get msgs::dataset_msg :definition-)
      "int32 id
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



(provide :msgs/dataset_msg "cc7ab277cce2b49147bf262deae10b1d")


