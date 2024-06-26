// Generated by gencpp from file msgs/dataset_array_msg.msg
// DO NOT EDIT!


#ifndef MSGS_MESSAGE_DATASET_ARRAY_MSG_H
#define MSGS_MESSAGE_DATASET_ARRAY_MSG_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <msgs/dataset_msg.h>

namespace msgs
{
template <class ContainerAllocator>
struct dataset_array_msg_
{
  typedef dataset_array_msg_<ContainerAllocator> Type;

  dataset_array_msg_()
    : data()
    , time()  {
    }
  dataset_array_msg_(const ContainerAllocator& _alloc)
    : data(_alloc)
    , time()  {
  (void)_alloc;
    }



   typedef std::vector< ::msgs::dataset_msg_<ContainerAllocator> , typename std::allocator_traits<ContainerAllocator>::template rebind_alloc< ::msgs::dataset_msg_<ContainerAllocator> >> _data_type;
  _data_type data;

   typedef ros::Time _time_type;
  _time_type time;





  typedef boost::shared_ptr< ::msgs::dataset_array_msg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::msgs::dataset_array_msg_<ContainerAllocator> const> ConstPtr;

}; // struct dataset_array_msg_

typedef ::msgs::dataset_array_msg_<std::allocator<void> > dataset_array_msg;

typedef boost::shared_ptr< ::msgs::dataset_array_msg > dataset_array_msgPtr;
typedef boost::shared_ptr< ::msgs::dataset_array_msg const> dataset_array_msgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::msgs::dataset_array_msg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::msgs::dataset_array_msg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::msgs::dataset_array_msg_<ContainerAllocator1> & lhs, const ::msgs::dataset_array_msg_<ContainerAllocator2> & rhs)
{
  return lhs.data == rhs.data &&
    lhs.time == rhs.time;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::msgs::dataset_array_msg_<ContainerAllocator1> & lhs, const ::msgs::dataset_array_msg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::msgs::dataset_array_msg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::msgs::dataset_array_msg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::msgs::dataset_array_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::msgs::dataset_array_msg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::msgs::dataset_array_msg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::msgs::dataset_array_msg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::msgs::dataset_array_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bbbdf2033e5021290631028b34c0b877";
  }

  static const char* value(const ::msgs::dataset_array_msg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbbbdf2033e502129ULL;
  static const uint64_t static_value2 = 0x0631028b34c0b877ULL;
};

template<class ContainerAllocator>
struct DataType< ::msgs::dataset_array_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "msgs/dataset_array_msg";
  }

  static const char* value(const ::msgs::dataset_array_msg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::msgs::dataset_array_msg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dataset_msg[] data\n"
"time time\n"
"\n"
"================================================================================\n"
"MSG: msgs/dataset_msg\n"
"int32 id\n"
"int32 lane_id\n"
"float32 length\n"
"float32 width\n"
"float64[] x\n"
"float64[] y\n"
"float64[] yaw\n"
"float64[] vx\n"
"float64[] vy\n"
"float64[] s\n"
"float64[] d\n"
"int32[] mask\n"
"int32 mode\n"
;
  }

  static const char* value(const ::msgs::dataset_array_msg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::msgs::dataset_array_msg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.data);
      stream.next(m.time);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct dataset_array_msg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::msgs::dataset_array_msg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::msgs::dataset_array_msg_<ContainerAllocator>& v)
  {
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::msgs::dataset_msg_<ContainerAllocator> >::stream(s, indent + "    ", v.data[i]);
    }
    s << indent << "time: ";
    Printer<ros::Time>::stream(s, indent + "  ", v.time);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MSGS_MESSAGE_DATASET_ARRAY_MSG_H
