# Provider


[文档](https://pub.dev/packages/provider)

---

### 不知道叫啥

### Provider

更新状态不更新UI

```dart
@override
Widget build(BuildContext context) {
    return Provider<Model模型>(
        create: (context) => Model模型(),
        child: MaterialApp()
    );
}
```

```dart title="model 模型"

class 模型Model{
  String name = '值';

  void 方法(){
    name = 'hello';
  }
}

```

### ChangeNotifierProvider

更新状态 更新UI

```dart
@override
Widget build(BuildContext context) {
    return ChangeNotifierProvider<Model模型>(
        create: (context) => Model模型(),
        child: MaterialApp()
    );
}
```

```dart title="model 模型"

class 模型Model extends ChangeNotifier{
  String name = '值';

  void 方法(){
    name = 'hello';
    notifyListeners ();  // 刷新UI
  }
}

```

### FutureProvider

只会重建一次, 使用默认值

```dart
@override
Widget build(BuildContext context) {
    return FutureProvider<Model模型>(
        initialData: Model模型(),  // 初始值
        create: (context) => asyncGetUserModel(),  // 返回 Model模型
        child: MaterialApp()
    );
}
```

```dart title="model 模型"
class 模型Model{
  String name = '值';

  void 方法(){
    name = 'hello';
  }
}
```

```dart
Future<UserModel> asyncGetUserModel() async{
    return UserModel(name: '获取新数据');
}
```



### StreamProvider

流对象

```dart
@override
Widget build(BuildContext context) {
    return StreamProvider<Model模型>(
        initialData: Model模型(),  // 初始值
        create: (context) => getStreamUserModel(),  // 返回 流 Model模型 
        child: MaterialApp()
    );
}
```

```dart title="model 模型"
class 模型Model{
  String name = '值';

  void 方法(){
    name = 'hello';
  }
}
```

```dart
Stream<UserModel> getStreamUserModel(){
    return Stream<UserModel>.periodic(Duration(microseconds: 1000),(value) => UserModel(name:'$value')).take(10);
}
```

---

## 消费者

```dart
Consumer<Model模型>(builder: (_, model实例, child) {
    return Text(model实例.属性);
}
```

## 生产者

```dart
Consumer<Model模型>(
    builder: (_, model实例, child) {
      return 按钮(
        onPressed: () => model实例.方法(),
      );
    }
)
```