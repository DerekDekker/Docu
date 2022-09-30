# Android组件

material 风格组件


`import 'package:flutter/material.dart';`

---
## MaterialApp

```dart
MaterialApp(
  debugShowCheckedModeBanner: false,  // Debug 关闭
  title: 'Welcome to Flutter',
  theme: ThemeData()  // 主题
  home: Scaffold()  // 主体
)
```

### ThemeData

主题配色

```dart
ThemeData(
    primarySwatch: Colors.blue,  // 主配色
)
```

---
## Scaffold

Scaffold 它提供了默认的导航栏、标题和包含主屏幕 widget

```dart
Scaffold(
    appBar: AppBar()  // 导航
    drawer: Drawer()  // 左侧抽屉
    body: 主体 
    floatingActionButton: FloatingActionButton()  // 右下角按钮 允许放其他组件
    extendBodyBehindAppBar: false,  // 是否允许AppBar透明
),
```

---
### Drawer

左侧抽屉

???abstract "演示"

    ```dart
    Drawer(
      // Add a ListView to the drawer. This ensures the user can scroll
      // through the options in the drawer if there isn't enough vertical
      // space to fit everything.
      child: ListView(
        // Important: Remove any padding from the ListView.
        padding: EdgeInsets.zero,
        children: [
          const DrawerHeader(
            decoration: BoxDecoration(
              color: Colors.blue,
            ),
            child: Text('Drawer Header'),
          ),
          Text('1'),
          Text('2')
        ],
      ),
    ),
    ```

---
## AppBar

顶部

```dart
AppBar(
    leading: const IconButton()  // 左侧
    title: Text()  // 标题 中间位置
    actions: [IconButton(), IconButton()],  // 右侧
    elevation: 0.0,  // 阴影
    centerTitle: true,  // 居中
),
```
## Divider

分割线

```yaml
Divider()
```

---
## 按钮

| 参数          | 描述                |
|-------------|-------------------|
| child       | 组件 一般放Text()      |
| onPressed   | 点击                |
| onLongPress | 长按                |
| style       | 样式 放ButtonStyle() |


### ElevatedButton

普通按钮

### OutlinedButton

轮廓按钮

### TextButton

文本按钮



### ButtonStyle

按钮样式

---
### IconButton

图标按钮


| 参数       | 描述       |
|----------|----------|
| tooltip  | 长安提示文本   |


```dart
IconButton(
  onPressed: () {  },
  icon: Icon(Icons.access_alarms_rounded),
),
```

---
## FloatingActionButton

悬浮按钮


| 参数          | 描述            |
|-------------|---------------|
| child       | 组件 一般放Text()  |
| tooltip       | 长安提示文本        |
| elevation       | 阴影            |



---
## 加载效果

### CircularProgressIndicator

```dart
CircularProgressIndicator()
```

---
## Text

```dart
Text(
    '内容',
    style: TextStyle(),  // 样式
    textDirection: TextDirection.ltr,  // 文本方向
    textAlign: TextAlign.center,  文本对齐
    maxLines: 3,  // 行数
    overflow: TextOverflow.ellipsis,  // 溢出方式
)
```

---
## CircleAvatar

头像

???abstract "代码"

    ```dart
    CircleAvatar(
      child: Text('我'),
      backgroundImage: AssetImage('assets/image/01.jpeg'),  // 图片
      backgroundColor: Colors.blueGrey,  // 颜色
      radius: 20,  // 大小
    )
    ```

---
## 图片


| 参数     | 描述  |
|--------|-----|
| width  | 宽度  |
| height | 高度  |


???abstract "参数"

    fit  显示方式
    
    `fit: BoxFit.cover`  覆盖

### Image.asset

显示本地图片

```dart
Image.asset('assets/image/01.jpeg')
```

### Image.network

网络图片

```dart
Image.network('URL')
```

---
## Icon

图标

```dart
Icon(Icons.图标名称, size: 30,)
```

---
## Chip

标签

```dart
Chip(
  label: Text('茶花'),
  avatar: Icon(Icons.add_location),  // 图标或头像
)
```

---
## AlertDialog

提示框

```dart
AlertDialog(
  title: Text('标题'),
  content: Text('提示内容'),
    actions: [  
      // 一般放按钮
    ]
)
```

---
## TextField

输入框


| 参数     | 描述      |
|--------|---------|
| autofocus  | 是否 获取焦点 |
| keyboardType | 键盘类型    |
| maxLength | 最多输入    |
| obscureText | 是否 密码形式 |
| maxLines | 最多几行    |
| onChanged | 输入事件    |
| decoration | 样式      |


```dart title="onChanged"
onChanged: (value) {
    // 执行代码
},
```

```dart title="decoration"
InputDecoration(
    prefix: Icon(Icons.mobile_screen_share),  // 图标
    label: Text('手机号'),  // 标题
    hintText: '请输入手机号',  // 提示
    // 获取焦点 样式
    focusedBorder: UnderlineInputBorder(
        borderSide: BorderSide(color: Colors.lightGreen),
    ),
    // 未获取焦点 样式
    enabledBorder: UnderlineInputBorder(
        borderSide: BorderSide(color: Colors.deepOrangeAccent),
    ),
    hintStyle: TextStyle()  // 提示文本样式
)
```

---
## Placeholder

占位 代表还未实现

---
## Divider

分割线


| 参数        | 描述  |
|-----------|-----|
| thickness | 厚度  |
| color     | 颜色  |

---
## TextField

文本域


| 参数            | 描述                 |
|---------------|--------------------|
| onTap         | 点击                 |
| autofocus     | 是否获取焦点             |
| decoration    | 样式 InputDecoration |

InputDecoration 样式

```dart
InputDecoration(
    // 边框
    enabledBorder: OutlineInputBorder(
      // 边角
      borderRadius: BorderRadius.all(
        Radius.circular(10),
      ),
      // 边框线
      borderSide: BorderSide(
        color: Color(0xfff4f6fa), // 边线颜色
        width: 1.5, // 粗细
      ),
    ),
    // 被选中样式
    focusedBorder: OutlineInputBorder(
        // 边框线
        borderSide: BorderSide(
          color: Color(0xfff4f6fa), //边框颜色为绿色
          width: 1.5, //宽度为5
        )
    ),
    // 填充颜色
    fillColor: Color(0xfff4f6fa),
    // 是否启动 填充颜色
    filled: false,
    // 标签文本 选中后会移到上方
    labelText: "用户名",
    // 提示文本 在下方显示
    helperText: "用户名或邮箱",
    // 提示文本 在输入框内显示 输入后消失
    hintText: "邮箱或ID",
    // 错误提示文本 在下方显示
    errorText: "errorText",
    // 图标
    prefixIcon: Icon(Icons.perm_identity),
)
```

输入框改变时

```dart
onChanged: (value){
    print('你输入的内容为$value');
}
```