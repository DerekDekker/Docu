官方
https://wiki.archlinux.org/index.php/Installation_guide_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)

文档
https://www.viseator.com/2017/05/17/arch_install/

视频
https://www.bilibili.com/video/av4058970/?p=2

----------------------------------------------------------最小系统
网络
wifi-menu

更新系统时间
# timedatectl set-ntp true


GPT分区
# gdisk /dev/sda
第1个分区 系统分区
#n
# 
# 
# +190G
# 
# p
第2个分区
# n
# 
#
# +2G
# 
# p
第3个分区
# n
# 
# 
# +300M
# l
# ef02
# p
第4个分区 交换分区 系统内存的二倍
#n
# 
# 
# +32G
# l
# 8200
# p
保存
# w
格式化
# mkfs.vfat /dev/sda3
# mkfs.ext4 /dev/sda1
# mkfs.ext4 /dev/sda2
# mkswap -f /dev/sda4
# swapon /dev/sda4
挂载系统
# mount /dev/sda1 /mnt
# mkdir /mnt/home
# mount /dev/sda2 /mnt/home
# mkdir /mnt/boot
# mkdir /mnt/boot/EFI
# mount /dev/sda3 /mnt/boot/EFI
安装基本包
# pacstrap /mnt base 或 pacstrap /mnt base base-devel
配置Fstab
# genfstab -U /mnt >> /mnt/etc/fstab
# cat /mnt/etc/fstab
切换到系统
# arch-chroot /mnt
设置语言 en_US.UTF-8 UTF-8     zh_CN.UTF-8 UTF-8 
# vi /etc/locale.gen
# locale-gen
# vi /etc/locale.conf
LANG=en_US.UTF-8
设置时间
# ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# hwclock --systohc
主机名
# vi /etc/hostname
# vi /etc/hosts
替换自己的做机名 2处
设置root密码
# passwd root
安装包
wifi
# pacman -S iw wpa_supplicant dialog
引导程序
# pacman -S grub efibootmgr
# grub-install --target=x86_64-efi --efi-directory=/boot/EFI --bootloader-id=grub
# grub-mkconfig -o /boot/grub/grub.cfg
退出系统
# exit
重启
# reboot

最小化系统完成安装

----------------------------------------------------------优化
CPU微码
pacman -S intel-ucode

显卡驱动
pacman -S nvidia

----------------------------------------------------------桌面安装
连接网络
# systemctl start dhcpcd
Xorg服务
# pacman -S xorg
安装 Gnome 桌面
# pacman -S gnome
登陆管理器
# systemctl enable gdm
# systemctl enable NetworkManager
创建登陆用户
# useradd -m -G wheel -s /bin/zsh xxx
# passwd xxx
# pacman -S zsh
权限
# pacman -S sudo
# visudo
82行的位置 %wheel ALL=(ALL)ALL

中文字体
# pacman -S wqy-zenhei

----------------------------------------------------------问题
gnome-software 
pacman -S gnome-software-packagekit-plugin

状态栏同步背景
https://blog.csdn.net/u010484267/article/details/25139469

中文输入
pacman -S ibus-googlepinyin

动态壁纸

登陆管理器
/usr/share/gnome-shell/theme

全局菜单


----------------------------------------------------------插件
美化
# pacman -S gnome-tweaks

终端
https://ohmyz.sh/
# sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
# vi .zshrc
# source .zshrc
pygmalion
sy
sunrise

底部
Dash to Dock

----------------------------------------------------------扩展
任务栏
Dash to dock

任务栏图标间距离
Status Area Horizontal Spacing

小图片
Toplcons Plus

顶部菜单栏
Gnome Global Application Menu

启用shell
User themes



TopIcons plus  状态栏小图标扩展

----------------------------------------------------------主题
图标
/usr/share/icons

主题
/usr/share/themes

----------------------------------------------------------使用
主题
https://www.gnome-look.org/p/1267246/

状态栏
https://www.gnome-look.org/p/1013030/

图标
https://www.gnome-look.org/p/1191167/

登录管理器
https://www.gnome-look.org/p/1241489/

开机动画
https://www.gnome-look.org/p/1200274/
https://www.gnome-look.org/p/1167904/
https://www.gnome-look.org/p/1200272/


----------------------------------------------------------pacman
源官网
http://mirrors.ustc.edu.cn/help/archlinuxcn.html

配置文件
/etc/pacman.conf

取消 # 注释
Color

[multilib]
Include = /etc/pacman.d/mirrorlist


尾部添加
[archlinuxcn]
Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch

运行
pacman -Syy
pacman -S archlinuxcn-keyring

----------------------------------------------------------yaourt
配置文件
/etc/yaourtrc

取消 # 注释并添加源
AURURL="https://aur.tuna.tsinghua.edu.cn"

yaourt -Syy





