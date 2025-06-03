/*
    Shubh Khandelwal
*/

#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/laser_scan.hpp>

class LaserScanNode : public rclcpp::Node
{

    private:

    enum
    {
        R = 0,
        FR = 1,
        F = 2,
        FL = 3,
        L = 4
    };

    rclcpp::Publisher<sensor_msgs::msg::LaserScan>::SharedPtr scan_publisher;
    rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr scan_subscriber;

    void scan_callback(const sensor_msgs::msg::LaserScan::SharedPtr msg)
    {
        std::vector<float> scan = msg->ranges;
        RCLCPP_INFO(this->get_logger(), "Laser scan size = %ld", scan.size());
        std::vector<float> filtered_scan(scan.begin(), scan.begin() + 120);
        sensor_msgs::msg::LaserScan filtered_msg = *msg;
        filtered_msg.angle_max = 2.0944;
        filtered_msg.ranges = filtered_scan;
        scan_publisher->publish(filtered_msg);
    }

    public:

    LaserScanNode() : Node("scan_node")
    {
        scan_publisher = this->create_publisher<sensor_msgs::msg::LaserScan>("/filtered_scan", 10);
        scan_subscriber = this->create_subscription<sensor_msgs::msg::LaserScan>("/scan", 10, std::bind(&LaserScanNode::scan_callback, this, std::placeholders::_1));
    }

};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<LaserScanNode>());
    rclcpp::shutdown();
    return 0;
}