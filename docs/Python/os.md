# OS

文件操作    执行命令

---

## 文件目录操作



`remove('文件名')`    删除文件

`rename('原文件','新名')`    重命名/移动



---

## 目录操作



`mkdir('目录名',权限)`    创建目录，权限可以空

`makedirs('目录名01/目录名02',权限)`    创建多级目录

`rmdir('目录名')`    删除目录

`removedirs('目录名')`    删除多级目录

`listdir('目录')`    返回指定目录下所有文件	注：'.'代表本目录

`getcwd()`    返回当前工作目录

`os.chdir('/root/www/')`  切换目录



---

## os.path



`abspath()`    返回绝对路径

`exists()`    判断文件是否存在

`getsize()`    返回文件大小

`isdir()`    判断是否是目录

`isfile()`    判断是否是文件

`splitext()`    分割文件扩展名

`urandom(长度int)`  随机数 操作系统提供的随机数生成器 可以应用于密码学



---

## 命令



`os.system('date')`    执行命令

`os.popen('dir').readlines()`    执行命令 返回列表

