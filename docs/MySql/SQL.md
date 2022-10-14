# SQL

---
## 增加

```sql
insert 表 values('值','值','值');

insert 表(列,列,列) values('值','值','值');

insert 表(列,列,列) values('值','值','值'),('值','值','值'),('值','值','值');

insert 表 set 列=值,列=值,列=值;
```


---
## 删除

```sql
delete from 表;

delete from 表 where 条件;

-- 清空表
truncate 表;
```


---
## 修改

```sql
update 表 set 列名='更新值';

update 表 set 列名='更新值' where 条件;
```

---
## 查询

```sql
select * from 表;

-- 只查询哪些字段
select 字段,字段 from 表;

 -- 其他数据库
select * from 库.表;

-- 别名
select 字段 as 别名,字段 as 别名 from 表 as 别名;
```


### 字段升序降序

```sql
-- 字段升序
order by 字段;

-- 字段降序
order by 字段 desc;
```

### 显示条数
```sql
limit 开始位置,条数;
```

---
## 条件

```sql
select * from 表 where 条件;

select * from 表 where 字段='值';
select * from 表 where 字段1='值' and 字段2='值';
select * from 表 where 字段1='值' or 字段2='值';
```

??? abstract "描述"

    写在 增 删 改 查 的语句后面


### 模糊匹配

like

```sql
select * from 表 where 字段 like '%值_';
select * from 表 where 字段 not like '%值_';
```

??? abstract "参数"

    % 0个或1个或多个任意字符

    _ 1个任意字符

### 范围

between 返回这个范围内的数据, 也可以为 not between 为相反

```sql
select * from 表 where 字段 between 2 and 3;
select * from 表 where 字段 not between 2 and 3;
```


### 集合

in 返回匹配这个集合内的数据, 也可以为 not in 为相反

```sql
-- 集合
select * from 表 where 字段 in('值1','值2');
select * from 表 where 字段 not in('值1','值2');

-- 正则表达式

```

### 正则表达式

regexp 待完善

```sql
select * from 表 where 字段 regexp '正则表达式';
```

### 表格

| 操作符            | 说明   |
|----------------|------|
| =              | 等号   |
| !=             | 不等于  |
| >              | 大于   |
| <              | 小于   |
| >=             | 大于等于 |
| <=             | 小于等于 |
| and            | 和    |
| or             | 或    |
| is not null    | 非空   |

---
## 分组

```sql
-- 统计字段出现的次数
SELECT 显示的字段, COUNT(*) FROM 表 GROUP BY 统计的字段;
```

---
## 多表查询

可以同时查询两个过更多表进行拼接

```sql
select * from 表
join 表
on 表.字段=表.字段
join 表
on 表.字段=表.字段
```

---
## 子查询

子查询就是在 where 后用()查询到的结果进行比较

```sql
select * from 外键表 where 外键值 in(select 主键值 from 主键表 where 条件)

select * from 外键表 where exists(select 主键值 from 主键表 where 条件)        
```


