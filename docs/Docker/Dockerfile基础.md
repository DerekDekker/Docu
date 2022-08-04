FROM ubuntu:latest    # FROM 系统:本版
ADD Holle.py /        # 添加文件 文件 容器内路径
CMD ["python3","Holle.py"]    # 命令