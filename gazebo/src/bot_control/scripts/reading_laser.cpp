#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/laser_scan.hpp>
#include <vector>

class LaserScanFilter : public rclcpp::Node
{
public:
    LaserScanFilter() : Node("laser_scan_filter")
    {
        
        subscription_ = this->create_subscription<sensor_msgs::msg::LaserScan>(
            "/scan", 10, std::bind(&LaserScanFilter::scan_callback, this, std::placeholders::_1));

        
        publisher_ = this->create_publisher<sensor_msgs::msg::LaserScan>("/filtered_scan", 10);
    }

private:
    void scan_callback(const sensor_msgs::msg::LaserScan::SharedPtr msg)
    {
        auto filtered_scan = *msg; 

        
        double min_angle = 0.0;              
        double max_angle = 120.0 * 3.14 / 180.0; 

        int start_index = (min_angle - msg->angle_min) / msg->angle_increment;
        int end_index = (max_angle - msg->angle_min) / msg->angle_increment;

        start_index = std::max(0, start_index);
        end_index = std::min(static_cast<int>(msg->ranges.size()) - 1, end_index);

        filtered_scan.ranges = std::vector<float>(msg->ranges.begin() + start_index, msg->ranges.begin() + end_index);
        filtered_scan.intensities = std::vector<float>(msg->intensities.begin() + start_index, msg->intensities.begin() + end_index);

        filtered_scan.angle_min = min_angle;
        filtered_scan.angle_max = max_angle;

        publisher_->publish(filtered_scan);
    }

    rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr subscription_;
    rclcpp::Publisher<sensor_msgs::msg::LaserScan>::SharedPtr publisher_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<LaserScanFilter>());
    rclcpp::shutdown();
    return 0;
}
