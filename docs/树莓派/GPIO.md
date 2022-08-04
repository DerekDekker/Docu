串口
/dev/ttyS0

USB转窜口
/dev/ttyUSB0

参看全部接口
ls -l /dev/tty*

获取串口数据
minicom -b 9600 -o -D /dev/ttyUSB0