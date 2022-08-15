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
## 基础

### 数据类型
```Dart
int 整型    double 小数    

String 字符串

[值, 值, 值] 列表    {'名城': 值,'名城': 值}  字典

```


???abstract "转换"

    int.parse('1'); // String -> int

    double.parse('1.1');  // String -> double

    1.toString();  // int -> String

    3.14159.toStringAsFixed(2);  // double -> String

### 变量定义
```Dart

var 名称;    声明变量 不需要指定变量类型

var 名称 = 'Voyager I';  不需要给定类型

final 名称;  只能赋值一次

const 名称 = 1;  只能声明时赋值

int? a;  初始值为空

int? a = 1;  可空

```


### 运算符

```dart
+ -  加减法	
++ 加等于
-- 减等于
== !=  相等判断	
&&  逻辑与	
||  逻辑或	
??  空判断

>    <    >=	<=	

	

```


### 赋值
```Dart

变量 ??= 3;  只在空的情况下赋值

+=

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
    
    as

    is  也可以是 is!	相反

### 流程控制语句

???abstract "if"

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

???abstract "switch"

    ```dart
    
    var command = 'OPEN';
    switch (command) {
      case 'CLOSED':
        executeClosed();
        break;
      case 'PENDING':
        executePending();
        break;
      case 'APPROVED':
        executeApproved();
        break;
      case 'DENIED':
        executeDenied();
        break;
      case 'OPEN':
        executeOpen();
        break;
      default:
        executeUnknown();
    }
    ```
---
## 数据类型
```Dart

变量.length  长度

```

### 字符串

多行变量


```dart
s1 = '''
你可以像这样创建多行字符串。
''';
```


不对转义符做处理

```dart

s = r'In a raw string, not even \n gets special treatment.';

```

### 列表

```Dart
变量[1]

列表.insert(1, 值)  插入

列表.remove(值)  删除

列表.clear(值)  清空

[0, ...列表]  合并列表 ...? 可为空列表
```

### 集合

创建集合

`var halogens = {'fluorine', 'chlorine', 'bromine', 'iodine', 'astatine'};`

```dart

[0, ...集合]  合并集合 ...? 可为空列表

`集合.add('fluorine');`  添加

`集合.length`  长度

```

### Maps

???abstract "创建"
    
    ```dart
    var gifts = {
      // Key:    Value
      'first': 'partridge',
      'second': 'turtledoves',
      'fifth': 'golden rings'
    };

    var nobleGases = {
      2: 'helium',
      10: 'neon',
      18: 'argon',
    };

    var gifts = Map<String, String>();
    gifts['first'] = 'partridge';
    gifts['second'] = 'turtledoves';
    gifts['fifth'] = 'golden rings';
    
    var nobleGases = Map<int, String>();
    nobleGases[2] = 'helium';
    nobleGases[10] = 'neon';
    nobleGases[18] = 'argon';
    ```

```dart

Maps[key] = 值;  新增

Maps.length  长度

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
void 名称(int 参数, String 参数 = 默认值, {可选参数, 可选参数}){
    // 代码
}

名称(参数, {可选参数, 可选参数}){
    // 代码
}

int 名称(参数, {可选参数, 可选参数}){
    // 代码
}
```


??? note "备注"

    void 不会返回值

    int 返回的类型


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

## 异常

```Dart

try {
    // 代码
} catch (e) {
    // 异常处理代码
}

```
