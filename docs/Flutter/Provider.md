# Provider


[文档](https://pub.dev/packages/provider)

---

## 提供者

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


### MultiProvider

多个

```dart
// ChangeNotifierProvider 可以是其他的

MultiProvider(
  providers: [
    ChangeNotifierProvider<Model模型1>(create: (context) => Model模型1()),
    ChangeNotifierProvider<Model模型2>(create: (context) => Model模型2()),
  ],
  child: MaterialApp(),
),
```


### ProxyProvider

将状态在提供者间共享 需要用到 MultiProvider

```dart

MultiProvider(
  providers: [
    ChangeNotifierProvider<Model模型1>(create: (_) => Model模型1()),  // 可以是其他提供者
    ProxyProvider<Model模型1, Model模型2>(
      update: (_, userModel5, walletModel) =>
          Model模型2(字段: Model模型1),  // 将 Model模型1 传递给 Model模型2
    )
  ],
  child: MaterialApp(),
)
```

### ChangeNotifierProxyProvider

和 `ProxyProvider` 原理一样, 区别在于它构建和同步 `ChangeNotifierProvider`, 当提供者数据变化时，将会重构UI

```dart
MultiProvider(
  providers: [
    Provider(create: (_) => Model模型1()),  // 可以是其他提供者
    ChangeNotifierProxyProvider<Model模型1, Model模型2>(
      create: (_) => Model模型2(Model模型1()),
      update: (_, model模型1, model模型2) => Model模型2(model模型1),
    )
  ],
  child: MaterialApp(),
)
```

```dart title="Model模型2"

class 模型Model2 extends ChangeNotifier{
  // 依赖的Model
  final Model模型1 model模型1;
  
  Model模型2(this.model模型1);

  String name = '值';

  void 方法(){
    name = 'hello';
    notifyListeners ();  // 刷新UI
  }
}

```


---
## 消费者

### Provider.of

```dart
Provider.of<CountNotifier1>(context);
Provider.of<CountNotifier1>(context,listen: false);

Provider.of<CountNotifier1>(context).属性
Provider.of<CountNotifier1>(context).方法()
```

### Consumer

可以在包裹的组件内使用属性或方法

```dart
Consumer<Model模型>(
    builder: (BuildContext context, model实例, child) {
      return Text(model实例.属性);
    }
)
```

不刷新的组件放到child来提升性能

```dart
Consumer<Model模型>(
    builder: (BuildContext context, model实例, child) {
      return child!;
    }
    child: 组件()  // 不刷新的组件
)
```

多个模型
```dart
// Consumer 有几个模型输入几 Consumer2 Consumer3 Consumer 4 最多为6

Consumer2<UserModel, UserModel2>(
  builder: (BuildContext context, userModel, userModel2, child) {
    return Text(userModel.name);
})
```


### Selector

不会更新全部值, 只会更新返回的值, 提升性能。 其他与 `Consumer` 类似, 

```dart
Selector<Model模型, 数据类型>(
  selector: (BuildContext context, model实例) => model实例.属性,  // 要返回的属性
  builder: (BuildContext context, 属性, child) {  // 属性为接收的属性
    return Text(属性.toString(),);
  },
  child: 组件,  // 不刷新的组件
)
```

---
## InheritedContext

### BuildContext.read

获取值, 但不会监听变化

```dart
final 名称 = context.read<Model模型>()();

名称.属性
名称.方法
```

### BuildContext.watch

监听变化

```dart
final 名称 = context.watch<Model模型>();

名称.属性
名称.方法
```

### BuildContext.select

与 Selector 相同, 名称等于属性值

```dart

final 名称 = context.select((Model模型 model实例) => model实例.属性);

```