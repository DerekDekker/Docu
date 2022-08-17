# Android组件

material 风格组件


`import 'package:flutter/material.dart';`

---
## MaterialApp

```dart
MaterialApp(
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

耳朵

```dart
AppBar(
  title: Text()  // 标题
),
```

---
## ListView.builder

| 参数           | 备注 |
|--------------|--|
| padding      | 内边距 |
| itemBuilder  | 组件 |
| itemCount  | 放入组件的数量 |


???abstract "代码"

    ```dart
    
    ListView.builder(
      padding: const EdgeInsets.all(16.0),
      itemBuilder: /*1*/ (context, i) {
        if (i >= _suggestions.length) {
          // 滑动到底时执行
        }
        
        // 返回的组件
        return Text(
            _suggestions[i].asPascalCase,
          );
      },
    )
    
    ```

---
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


