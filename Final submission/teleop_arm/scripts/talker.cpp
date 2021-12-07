#include "ros/ros.h"
#include "std_msgs/Float64.h"
#include "sensor_msgs/Joy.h"

class Controller
{
private:
    
    void joyCallback(const sensor_msgs::Joy::ConstPtr& joy);

    ros::NodeHandle n;

    int linear_, angular_;
    double l_scale_, a_scale_;
    
    ros::Publisher vel_pub;

    ros::Subscriber vel_sub;

public:
    Controller();
};

Controller::Controller():
    linear_(1),
    angular_(2)
{
    n.param("axis_linear", linear_, linear_);
    n.param("axis_angular", angular_, angular_);
    n.param("scale_angular", a_scale_, a_scale_);
    n.param("scale_linear", l_scale_, a_scale_);

    vel_pub = n.advertise<std_msgs::Float64>("chatter",1);

    vel_sub = n.subscribe<sensor_msgs::Joy>("joy", 10, &Controller::joyCallback, this);

}

void Controller::joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
{
    std_msgs::Float64 val1;//, val2;
    val1.data = a_scale_ * joy->axes[angular_];
    //val2.data = l_scale_ * joy->axes[linear_];
    
    vel_pub.publish(val1);
}

int main(int argc, char** argv)
{
    ros::init(argc,argv, "talker");
    
    Controller pos;

    ros::spin();
}