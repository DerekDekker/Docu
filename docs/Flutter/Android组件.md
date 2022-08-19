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

| 参数          | 描述                 |
|-------------|--------------------|
| child       | 组件 一般放Text()       |
| onPressed   | 点击                 |
| onLongPress | 长按                 |
| style       | 样式 放ButtonStyle()  |


### ElevatedButton

普通按钮

### OutlinedButton

轮廓按钮

### TextButton

文本按钮

### IconButton

图标按钮

### FloatingActionButton

悬浮按钮

### ButtonStyle

按钮样式

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
## Image.asset

显示本地图片

```dart
Image.asset('assets/image/01.jpeg', width: 50)
```

???abstract "参数"

    fit  显示方式
    
    `fit: BoxFit.cover`  覆盖



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