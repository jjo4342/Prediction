;; Auto-generated. Do not edit!


(when (boundp 'msgs::map_msg)
  (if (not (find-package "MSGS"))
    (make-package "MSGS"))
  (shadow 'map_msg (find-package "MSGS")))
(unless (find-package "MSGS::MAP_MSG")
  (make-package "MSGS::MAP_MSG"))

(in-package "ROS")
;;//! \htmlinclude map_msg.msg.html


(defclass msgs::map_msg
  :super ros::object
  :slots (_path_id _left_path_id _right_path_id _succesors _predecessors _center ))

(defmethod msgs::map_msg
  (:init
   (&key
    ((:path_id __path_id) 0)
    ((:left_path_id __left_path_id) 0)
    ((:right_path_id __right_path_id) 0)
    ((:succesors __succesors) (make-array 0 :initial-element 0 :element-type :integer))
    ((:predecessors __predecessors) (make-array 0 :initial-element 0 :element-type :integer))
    ((:center __center) ())
    )
   (send-super :init)
   (setq _path_id (round __path_id))
   (setq _left_path_id (round __left_path_id))
   (setq _right_path_id (round __right_path_id))
   (setq _succesors __succesors)
   (setq _predecessors __predecessors)
   (setq _center __center)
   self)
  (:path_id
   (&optional __path_id)
   (if __path_id (setq _path_id __path_id)) _path_id)
  (:left_path_id
   (&optional __left_path_id)
   (if __left_path_id (setq _left_path_id __left_path_id)) _left_path_id)
  (:right_path_id
   (&optional __right_path_id)
   (if __right_path_id (setq _right_path_id __right_path_id)) _right_path_id)
  (:succesors
   (&optional __succesors)
   (if __succesors (setq _succesors __succesors)) _succesors)
  (:predecessors
   (&optional __predecessors)
   (if __predecessors (setq _predecessors __predecessors)) _predecessors)
  (:center
   (&rest __center)
   (if (keywordp (car __center))
       (send* _center __center)
     (progn
       (if __center (setq _center (car __center)))
       _center)))
  (:serialization-length
   ()
   (+
    ;; int16 _path_id
    2
    ;; int16 _left_path_id
    2
    ;; int16 _right_path_id
    2
    ;; int16[] _succesors
    (* 2    (length _succesors)) 4
    ;; int16[] _predecessors
    (* 2    (length _predecessors)) 4
    ;; msgs/point_msg[] _center
    (apply #'+ (send-all _center :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _path_id
       (write-word _path_id s)
     ;; int16 _left_path_id
       (write-word _left_path_id s)
     ;; int16 _right_path_id
       (write-word _right_path_id s)
     ;; int16[] _succesors
     (write-long (length _succesors) s)
     (dotimes (i (length _succesors))
       (write-word (elt _succesors i) s)
       )
     ;; int16[] _predecessors
     (write-long (length _predecessors) s)
     (dotimes (i (length _predecessors))
       (write-word (elt _predecessors i) s)
       )
     ;; msgs/point_msg[] _center
     (write-long (length _center) s)
     (dolist (elem _center)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _path_id
     (setq _path_id (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _left_path_id
     (setq _left_path_id (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _right_path_id
     (setq _right_path_id (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16[] _succesors
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _succesors (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _succesors i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;; int16[] _predecessors
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _predecessors (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _predecessors i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     ))
   ;; msgs/point_msg[] _center
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _center (let (r) (dotimes (i n) (push (instance msgs::point_msg :init) r)) r))
     (dolist (elem- _center)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get msgs::map_msg :md5sum-) "74bec9aa085584f3c79b706501e2c126")
(setf (get msgs::map_msg :datatype-) "msgs/map_msg")
(setf (get msgs::map_msg :definition-)
      "int16 path_id
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



(provide :msgs/map_msg "74bec9aa085584f3c79b706501e2c126")


