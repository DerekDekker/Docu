# bloc

[官方](https://bloclibrary.dev)

[文档](https://pub.dev/packages/flutter_bloc)

这IDE里可以安装 bloc 插件, 方便开发.

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