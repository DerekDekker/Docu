# SQL


---
## 查

```sql
SELECT 字段, 字段 FROM 表;

SELECT * FROM 表;
```

## 增

```sql
INSERT INTO 表 (字段, 字段) VALUES (值, 值);

INSERT INTO user VALUES (值, 值);
```

## 删

```sql
DELETE FROM 表
```


## 改

```sql
UPDATE 表 SET 字段=值, 字段=值;
```

## 条件

链接符号可以是 AND 或 OR

```sql
WHERE 字段='值' 链接符号 字段='值';
```

算术运算符

```sql
SELECT * FROM 表 WHERE 字段 运算符 值;

-- 演示
SELECT * FROM user WHERE age < 20+age;
```


## LIKE

模糊查询, 加在  `WHERE` 条件后面

%    零个 一个 多个

_    一个

```sql
SELECT * FROM user WHERE 字段 LIKE '%值%';
```


## GLOB

匹配, 加在  `WHERE` 条件后面, 大小写敏感

```
*    零个 一个 多个

?    一个
```


```sql
SELECT * FROM 表 WHERE 字段 GLOB '值*';

```

## LIMIT

设置返回的数量

```sql
SELECT * FROM 表 LIMIT 2

```

返回数量 与 截取位置

```sql
SELECT * FROM 表 LIMIT 2 OFFSET 2;
```


## 排序

默认升序

```sql
SELECT * FROM 表 ORDER BY 字段, 字段;
```

### 降序 DESC

```sql
SELECT * FROM 表 ORDER BY 字段 DESC, 字段 DESC;
```

## DISTINCT


重复数据只返回一条

```sql
SELECT DISTINCT 字段, 字段 FROM 表
```

---
## 子查询

() 里面查询出来的值作为条件

```sql
SELECT * FROM 表 WHERE 字段 IN (值, 值);

```

演示 查

```sql
SELECT * FROM user WHERE age = (SELECT age FROM user WHERE name GLOB '小*');
```


演示 改

```sql
UPDATE user SET age = age * 0.50 
WHERE age IN (SELECT age FROM user
WHERE age >= 27);
```

演示 删

```sql
DELETE FROM user
WHERE age IN (SELECT date FROM holiday
WHERE date > 27);
```







