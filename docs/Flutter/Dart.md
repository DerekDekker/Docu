# Dart

[官网](https://dart.cn/)

---
## 主入口

```Dart
main(){
    // 代码
}
```


---
## 数据类型
```Dart
int 整型    double 小数    

String 字符串

Booleans 布尔

[值, 值, 值] 列表    {'名城': 值,'名城': 值}  字典

```

### 变量定义

```Dart
var 名称;    不需要给定类型

final 名称;  只能赋值一次

const 名称 = 1;  只能声明时赋值

数据类型 名称;  指定数据类型

```

---
### 空安全

```dart
int? a;  初始值为空

int? a = 1;  可空
```

---
### 运算符

```dart
+ - * /
++ 加等于 1
-- 减等于 1
+= 加等于
-= 减等于
! 取反
== !=  相等判断
&&  逻辑与
||  逻辑或	
??  空判断

>    <    >=	<=	

```

### 表达式
```Dart
变量 ??= 值;  只在空的情况下赋值

变量1 ?? 变量2  左边表达式返回空值，则会返回右边的表达式
变量1 ?? 变量2 ?? 变量3

表达式 ? 值1 : 值2    表达式如果为true则 返回 值1 否则 返回 值2  

:    =>


```


#### 箭头语法

该函数将在其右侧执行表达式并返回其值

`name => 1+1;`

---
## 语法
!!! abstract "备注"

    `print();`    打印
    
    as

    is  也可以是 is!	相反

### 流程控制语句

???abstract "if"

    ```Dart
    判断
    if (条件) {
      // 代码
    } else if (条件) {
      // 代码
    } else {
      // 代码
    }
    
    ```

???abstract "for"

    ```dart
        遍历循环
        for (final 名称 in 可迭代变量) {
          print(名称);
        }
        
        循环
        for (int month = 1; month <= 12; month++) {
          print(month);
        }
    ```

    break  结束循环

    continue  结束本次循环


???abstract "while"

    ```dart
        循环
        while (条件) {
          year += 1;
        }
    ```

    break  结束循环

    continue  结束本次循环


???abstract "switch"

    ```dart
    switch (变量) {
      case '值':
        // 代码
        break;
      case '值':
        // 代码
        break;
      default:
        // 代码
    }

???abstract "try"

    ```dart
    try {
        // 代码
    } catch (e) {
        // 异常处理代码
    }
    ```

---
### 函数

```dart
名称(参数, {可选参数, 可选参数}){
    // 代码
}
```

#### 无返回值
```Dart
void 名称(int 参数, String 参数 = 默认值, {可选参数, 可选参数}){
    // 代码
}


```

#### 数据类型

规定返回的数据类型

```dart
数据类型 名称(参数, {可选参数, 可选参数}){
    // 代码
}
```



```Dart
// 可选参数

int sumUpToFive(int a, [int? b, int? c, int? d, int? e]) {
  int sum = a;
  if (b != null) sum += b;
  if (c != null) sum += c;
  if (d != null) sum += d;
  if (e != null) sum += e;
  return sum;
}

```

```

```Dart
void 名称() => 表达式

调用
方法(值, 可选参数名:值)
```

---
## 面向对象


```Dart
实例化

类名 名称 = 类()

var 名称 = 类()

```

```Dart

class 名称 {
  String? name;  // 属性
  int? _age;  // 私有属性
  DateTime? launchDate;
  
  // 只读非最终属性
  int? get launchYear => launchDate?.year;
  
  // 构造方法
  类名(this.name, this.launchDate, string a) {
    // 初始化代码
    this.a = a
  }

  // 构造方法接收的参数
  类名.unlaunched(String name) : this(name, null);
  
  
  // 使用 this
  类名(this.red, this.green, this.blue);
  

  // 私有方法
  void _run(参数, 参数) {
    print('name$name age$age');
  }

  // 静态方法
  static int sum(){
    // 代码块
  }
}

```

### 继承

```Dart
class 名称 extends 继承的类(){
  @override  // 重写父类方法
  方法
}
```

### 多继承
```Dart
class 名称 implements 继承的类, 继承的类(){
  @override  // 重写父类方法
  方法
}
```

### 抽象方法

```Dart

抽象方法
abstract class 名称{}

```

