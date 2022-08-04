--------------------------------------------------------------GPS
sudo modprobe option
sudo chmod 777 /sys/bus/usb-serial/drivers/option1/new_id
echo 1782 4e00 > /sys/bus/usb-serial/drivers/option1/new_id
sudo minicom -s
    Serial port setup
    Exit

at+cgnspwr=1
at+cgnsaid=31,1,1,1
三分钟后

at+cgnsinf
at+cgnsurc=1

关闭GPS
at+cgnsurc=0
at+cgnspwr=0
