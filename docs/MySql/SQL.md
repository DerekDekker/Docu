# SQL

---
## 增加

```mysql
insert 表 values(值,值,值);

insert 表(列,列,列) values('值','值','值');

insert 表(列,列,列) values('值','值','值'),('值','值','值'),('值','值','值');

insert 表 set 列=值,列=值,列=值;
```


---
## 删除

```mysql
delete from 表;

delete from 表 where 条件;

-- 清空表
truncate 表;
```


---
## 修改

```mysql
update 表 set 列名='更新值';

update 表 set 列名='更新值' where 条件;
```

---
## 查询

```mysql
select * from 表;

-- 只查询哪些字段
select 字段,字段 from 表;

 -- 其他数据库
select * from 库.表;

-- 别名
select 字段 as 别名,字段 as 别名 from 表 as 别名;
```


### 加在查询后面

```mysql
-- 字段升序,加 desc 降序
order by 字段 desc;

-- 显示条数,一个数值代表前几个条数
limit 开始位置0,条数;
```

---
## 条件

```mysql
select * from 表 where 条件;

-- 范围
字段 not between 2 and 3;

-- 集合
字段 not in('值','值');

-- 正则表达式
字段 regexp '正则表达式';
```


=       !=       >       >=       and       or       is not null


########################################### 模糊匹配
select * from 表 where 字段 not like '%值_'
%:0个或1个或多个任意字符
_:1个任意字符

---
## 分组

select * from 表 group by 字段

select 字段,group_concat(字段) from 表 group by 字段       --显示某字段详情

select 字段,count(*) from 表                               --显示分组数   更多max(字段),min(字段),avg(字段),sum(字段)

having count(*)>2                                          --筛选


---
## 多表查询

"可以同时查询两个过更多"
select * from 表
join 表
on 表.字段=表.字段
join 表
on 表.字段=表.字段

leif join 代表左表为主表

---
## 子查询

"子查询就是在 where 后用()查询到的结果进行比较"
select * from 外键表 where 外键值 in(select 主键值 from 主键表 where 条件)

select * from 外键表 where exists(select 主键值 from 主键表 where 条件)            --子查询能查到数据在执行下面操作

-------------------------------------------------------函数
now()                   --当前日期时间, 可以用于插入数据


---
## 存储过程

'''
方式    in 输入    out 输出    inout 输入输出
'''
create procedure 名称(方式 变量 类型)
begin
    //代码
end;

call 过程(参数)             --调用存储过程

select 变量                 --查询变量

set 变量 = 值               --变量赋值

declare 变量 int default 默认值;         --变量定义


+++++++++++++++++++++++++++++++++++++++++++ 错误处理
'出现错误后依然可以执行接下来的代码, set 后的变量当代码错误时被赋值'
declare continue handler for sqlstate '错误代码' set @变量=值;

########################################### 操作
show procedure status                   --查看存储过程, 可以加上 where db='数据库名'

show create procedure 存储过程          --查看存储过程

drop procedure 存储过程                 --删除存储过程

---
## 流程扩展

if 条件 then
    //代码
elseif 多条件 then
     //代码
else
     //代码
end if;


while 条件 do
    //代码
end while;


---
## 视图

create view 名称
as
查询语句

drop view 视图                        --删除


---
## 触发器

create trigger 名称 after insert
on 表 for each row
begin
    //代码
    insert wages(student_id,money) values(new.id,10);
end;

定义
create trigger 名称 先后执行 事件类型

+++++++++++++++++++++++++++++++++++++++++++ 代码区
先后执行
after    --事件之后
before   --事件之前

事件类型
insert    delete    update

新数据
new.字段

老数据
old.字段

########################################### 操作
drop trigger 触发器           --删除


---
## 事务

start transaction              --开启事务

commit                         --提交

rollback                       --回滚


---
## 定时器

create event 名称 on schedule every 时间 单位 多选
do
begin
    //代码
end;

--时间单位
second              --秒

minute              --分

day                 --天

month               --月

--多选
starts '2013-01-13 00:00:00'                    --开始时间

starts timestamp (current_date(),'00:00:30')    --在此时间执行, 如1分钟执行一次 00:00:30 代表每1分钟在世界时间的30秒时执行


########################################### 操作
alter event 定时器 disable             --关闭

alter event 定时器 enable              --启动

drop event 定时器                      --删除

show events                            --当前所有定时器

show create event 定时器               --查看定时器


---
## 演示

'''
    存储过程配合事务
    代码部分只要有错误就回滚事务
'''
create procedure 名称()
begin
    declare t_error integer default 0;
    declare continue handler for sqlexception set t_error=1;
    start transaction;

    //代码

    if t_error = 1 then
        rollback ;
    else
        commit ;
    end if;
end;