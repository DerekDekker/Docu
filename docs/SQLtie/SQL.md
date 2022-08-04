数据类型


存储类
NULL 指定该值为空值
INTEGER 有符号整数 可用于自增
REAL 浮点
text 文本字符串
BLOB 数据快

date
time
datetime


----------------------------算术运算符
运算符
+    -    *    /    %

比较运算符
=    ==    !=    <    >    <=    >=

逻辑
AND ORD UNIQUE NOT IN


----------------------------查
-- * 可以代替字段
SELECT 字段, 字段 FROM 表;


----------------------------增
INSERT INTO 表 (字段, 字段)
VALUES (值, 值);

INSERT INTO user VALUES (值, 值);


----------------------------删
DELETE FROM 表


----------------------------改
UPDATE 表 SET 字段=值, 字段=值;


----------------------------条件
-- 链接符号    AND    OR
WHERE 字段='值' 链接符号 字段='值';

-- 算术运算符
SELECT * FROM 表 WHERE 字段 运算符 值;

-- 演示
SELECT * FROM user WHERE age < 20+age;


----------------------------LIKE
匹配
%    零个 一个 多个
_    一个

WHERE 字段 LIKE '%值%'


----------------------------GLOB
匹配
大小写敏感
*    零个 一个 多个
?    一个

SELECT * FROM 表 WHERE 字段 GLOB '值*';


----------------------------LIMIT
返回数量
SELECT * FROM 表 LIMIT 2

返回数量 与 截取位置
SELECT * FROM 表 LIMIT 2 OFFSET 2;


----------------------------排序
默认升序
SELECT * FROM 表 ORDER BY 字段, 字段;

降序 DESC
SELECT * FROM 表 ORDER BY 字段 DESC, 字段 DESC;

----------------------------DISTINCT
重复数据只返回一条
SELECT DISTINCT 字段, 字段 FROM 表


----------------------------子查询
() 里面查询出来的值作为条件

SELECT * FROM 表 WHERE 字段 IN (值, 值);

-- 演示 查
SELECT * FROM user WHERE age = (SELECT age FROM user WHERE name GLOB '小*');

-- 演示 改
UPDATE user SET age = age * 0.50 
WHERE age IN (SELECT age FROM user
WHERE age >= 27);

-- 演示 删
DELETE FROM user
WHERE age IN (SELECT date FROM holiday
WHERE date > 27);






