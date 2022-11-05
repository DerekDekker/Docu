# Join


---
## 交叉连接 CROSS JOIN

```sql
SELECT * FROM 表1 CROSS JOIN 表2;
```


## 内连接 INNER JOIN

找到所有满足连接谓词的行的匹配对

```sql
SELECT * FROM 表1 INNER JOIN 表2 ON 表1.字段 = 表2.字段;

```


## 外连接 OUTER JOIN

未匹配的值会用NULL代替

```sql
SELECT * FROM 表1 LEFT OUTER JOIN 表2 ON 表1.字段 = 表2.字段;
```




