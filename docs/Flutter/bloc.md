# bloc

[官方](https://bloclibrary.dev)

[文档](https://pub.dev/packages/flutter_bloc)

这IDE里可以安装 bloc 插件, 方便开发.

---
## 安装

```yaml
bloc: ^8.0.0
flutter_bloc: ^8.0.0
```

---
## Cubit


定义一个 Cubit, 代码生成快捷键 cubit
```dart
// 定义了一个只能接收 int 的 cubit, 也可以是类
class CounterCubit extends Cubit<int> {
  CounterCubit() : super(0);  // super(0) 状态默认值
  
  // increment 定义一个公共方法
  void increment() => emit(state + 1);  // state 获取当前状态, emit更改当前状态
  
  // 每次状态变化时都会被调用 状态还未改变前
  @override
  void onChange(Change<int> change) {
    // super.onChange(change);
    print(change);
  }
  
  // 错误发生时被调用
  @override
  void onError(Object error, StackTrace stackTrace) {
    print('$error, $stackTrace');
    super.onError(error, stackTrace);
  }
}
```

```dart
// 接收参数 
class CounterCubit extends Cubit<int> {
  CounterCubit(int initialState) : super(initialState);
}
```

```dart
// 实力化
final cubitA = CounterCubit(参数);

// 状态发生变化后调用这个函数 并且会传变化后的值
cubit.stream.listen(函数)

// 当前状态值
cubit.stream


// 关闭内部状态流 关闭后不能更改状态
cubit.close();
```

---
## Bloc

```dart
abstract class CounterEvent {}
class CounterIncrementPressed extends CounterEvent {}

class CounterBloc extends Bloc<CounterEvent, int> {
  CounterBloc() : super(0) {
    
    // 用于刷新值
    on<CounterIncrementPressed>((event, emit) {
      print(event);  // 获取传进的类
      emit(state + 1);  // 更改状态
    });
  }
  
  // 状态变化时被调用 只会获取到变化的数字 状态还未改变前
  @override
  void onChange(Change<int> change) {
    super.onChange(change);
    print(change);
  }
  
  // 状态变化时被调用 状态还未改变前
  @override
  void onTransition(Transition<CounterEvent, int> transition) {
    super.onTransition(transition);
    print(transition);
  }
  
  // 事件传入时被执行
  @override
  void onEvent(CounterEvent event) {
    super.onEvent(event);
    print(event);
  }
  
  // 错误发生时被调用
  @override
  void onError(Object error, StackTrace stackTrace) {
    print('$error, $stackTrace');
    super.onError(error, stackTrace);
  }
}
```

```dart
// 实力化
final bloc = CounterBloc();

// 当前状态
bloc.state

// 刷新状态
bloc.add(CounterEvent());

// 状态发生变化后调用这个函数 并且会传变化后的值
bloc.stream.listen(函数);

// 等等执行完成 以确保我们等待下一个事件
await Future.delayed(Duration.zero);
```

---
## BlocObserver

观察者, 负责观察全局的状态变化, 代码生成快捷键 blocobserver


```dart
class SimpleBlocObserver extends BlocObserver {
  
  // 状态变化时被调用 只会获取到变化的数字 状态还未改变前
  @override
  void onChange(BlocBase bloc, Change change) {
    super.onChange(bloc, change);
    print('${bloc.runtimeType} $change');
  }
  
  // 状态变化时被调用 状态还未改变前
  @override
  fvoid onTransition(Bloc bloc, Transition transition) {
    super.onTransition(bloc, transition);
    print('${bloc.runtimeType} $transition');
  }
  
  // 错误发生时被调用
  @override
  void onError(BlocBase bloc, Object error, StackTrace stackTrace) {
    print('${bloc.runtimeType} $error $stackTrace');
    super.onError(bloc, error, stackTrace);
  }
  
  // 事件传入时被执行 状态还未改变前
  @override
  void onEvent(Bloc bloc, Object? event) {
    super.onEvent(bloc, event);
    print('${bloc.runtimeType} $event');
  }

}
```

```dart
// 实力化
Bloc.observer = SimpleBlocObserver();
```

---
## 项目结构

???abstract "目录结构"

    main.dart  主文件

    app.dart 

    页面名

    页面名/bloc

    页面名/bloc/页面名_bloc.dart

    页面名/bloc/页面名_event.dart

    页面名/bloc/页面名_state.dart

    页面名/view

    页面名/view/页面名_page.dart

    页面名/view/页面名_view.dart


### main.dart


```dart title="main.dart"
void main() {
  Bloc.observer = CounterObserver();  // BlocObserver 观察者
  runApp(const CounterApp());
}
```

### app.dart

里面有 MaterialApp 组件

```dart title="app.dart"
class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Timer',
      home: const CounterPage(),
    );
  }
}
```

### counter_page.dart

```dart
class CounterPage extends StatelessWidget {
  const CounterPage({super.key});

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (_) => CounterCubit(),  // Bloc
      child: const CounterView(),  // 视图
    );
  }
}
```

---
## flutter_bloc

### BlocBuilder

状态改变时刷新组件

```dart
BlocBuilder<CounterCubit类, int>(
    builder: (context, count) => Text('$count'),
),
```

```dart
BlocBuilder<Bloc类, State类>(
    builder: (context, count) => Text('$count'),
),
```

### BlocProvider

可以将一个bloc的单个实例提供给子树中的多个部件

```dart
BlocProvider(
  create: (_) => BlocA(),  // Bloc累
  child: ChildA(),  // 组件
);
```

---
## 项目代码

### Cubit

```dart
class CounterCubit extends Cubit<int> {
  CounterCubit() : super(0);

  void increment() => emit(state + 1);
  void decrement() => emit(state - 1);
}
```

### bloc类

```dart
class PostBloc类 extends Bloc<PostEvent事件类, PostState状态类> {
  PostBloc类() : super(const PostState状态类()) {
    on<TimerStarted事件子类>(_onStarted);
    on<TimerPaused事件子类>(_onPaused);
    on<TimerResumed事件子类>(_onResumed);
    on<TimerReset事件子类>(_onReset);
    on<TimerTicked事件子类>(_onTicked);
  }
  
  // 一个方法
  void _onStarted(TimerStarted事件子类 event, Emitter<TimerState状态类> emit) {
    emit(TimerRunInProgress(event.duration));  // 更新状态
    TimerStarted事件子类.属性  // 获取事件参数
  }
  
}
```

### Event事件

```dart
abstract class PostEvent extends Equatable {
}

class PostFetched extends PostEvent {}
```

```dart
@immutable
abstract class GpsEvent {
  const GpsEvent();
}

class GpsInitialization extends GpsEvent {}

class GpsUpdate extends GpsEvent {
  const GpsUpdate({required this.gpsModel});
  final GpsModel gpsModel;  // 参数
}
```

### Status状态

```dart
enum PostStatus { initial, success, failure }

class PostState extends Equatable {
  const PostState({
    this.status = PostStatus.initial,
    this.posts = const <Post>[],
    this.hasReachedMax = false,
  });

  final PostStatus status;
  final List<Post> posts;
  final bool hasReachedMax;
  
  @override
  String toString() {
    return '''posts: ${posts.length} }''';
  }
}
```

---
## 使用

### 使用函数

```dart
context.read<Cubit类>().方法()
```

可以不传参数

```dart
context.read<Bloc类>().add(事件(参数: 值))
```

### Bloc获取状态

状态发生改变时 这个变量值也会改变

```dart
final duration = context.select((Bloc类 bloc) => bloc.state.状态变量);
```