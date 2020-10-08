#include<ros/ros.h>
#include <std_msgs/Int64.h>
#include <stdlib.h>
#include <string>

/*class Bus{
    private:
        static ros::NodeHandle nh;
        static ros::Publisher pub;
        static ros::Subscriber sub;
        static int acc;

    public:
        static void callback_receive_number(const std_msgs::Int64 & msg_in);
        static void init(void);
};

void Bus::callback_receive_number(const std_msgs::Int64 & msg_in) {
    Bus::acc += int(msg_in.data);
    ROS_INFO("ACC = %d", Bus::acc);
    std_msgs::Int64 msg_out;
    Bus::pub.publish(msg_out);
}

void Bus::init(void) {
    Bus::pub = Bus::nh.advertise<std_msgs::Int64>(
        "/number_count", 10
    );
    Bus::sub = Bus::nh.subscribe(
        "/number", 1000, 
        Bus::callback_receive_number
    );
    Bus::acc = 0;
}*/

int main (int argc, char **argv) {
    ROS_INFO("number_counter");
    ros::init(argc, argv, "number_counter");

    //Bus::init();

    ros::spin();
}


