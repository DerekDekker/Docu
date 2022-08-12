# Dart

---
## 主入口

```Dart
main(){
    // 代码
}
```


---
## 基础

### 数据类型
```Dart
int 整型    double 小数    String 字符串

[值, 值, 值] 列表    {'名城': 值,'名城': 值}  字典

```

### 变量定义
```Dart

var 名称;    声明变量

var 名称 = 'Voyager I';  不需要给定类型

final 名称;  只能赋值一次

const 名称 = 1;  只能声明时赋值

int? a;  初始值为空

int? a = 1;  可空

```


### 运算符


### 赋值
```Dart

变量 ??= 3;  只在空的情况下赋值

```

### 表达式
```Dart

??  1 ?? 3  左边表达式返回空值，则会返回右边的表达式

:    =>

'XXXXX$变量'  拼接变量
'${3 + 2}'  运算
'${"word".toUpperCase()}'  表达式

类?.属性  可能为空的属性正常访问, 点（.）之前加一个问号（?）
```


#### 箭头语法

该函数将在其右侧执行表达式并返回其值

`name => 1+1;`

---
## 语法
!!! abstract "备注"

    `print();`    打印

### 流程控制语句

```Dart
判断
if (year >= 2001) {
  print('21st century');
} else if (year >= 1901) {
  print('20th century');
}

遍历循环
for (final object in flybyObjects) {
  print(object);
}

循环
for (int month = 1; month <= 12; month++) {
  print(month);
}

循环
while (year < 2016) {
  year += 1;
}
```

---
## 数据类型
```Dart

变量.toInt()  转整形

变量.toString()  转字符串

变量.length  长度

```

### 列表

```Dart
变量[1]

列表.insert(1, 值)  插入

列表.remove(值)  删除

列表.clear(值)  清空
```

### Iterable

可迭代集合 适用于全部可迭代对象

可以直接参与 for 遍历


定义

`Iterable<String> iterable = const ['Salad', 'Popcorn', 'Toast'];`

```Dart

iterable.elementAt(1);  访问下标
iterable.first;  访问第一个元素
iterable.last;  访问最后一个元素

```

---
### 函数

```Dart

函数
void 名称(参数, {可选参数, 可选参数}){
    // 代码
}
```

```Dart
函数
名称(参数, {可选参数, 可选参数}){
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

```Dart
指定类型
int fibonacci(int n) {
  return n;
}

var result = fibonacci(20);

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
```

```Dart

class 名称 {
  String? name;  // 属性
  int? _age;  // 私有属性
  DateTime? launchDate;
  
  // 只读非最终属性
  int? get launchYear => launchDate?.year;
  
  // 构造方法
  类名(this.name, this.launchDate) {
    // 初始化代码
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

## 异常

```Dart

try {
    // 代码
} catch (e) {
    // 异常处理代码
}

```
