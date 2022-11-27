# 建造者

!!! none ""

    创建一系列复杂对象

    控制顺序

---

## 产品 
```python
class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return f'{self.face} {self.body} {self.arm} {self.leg}'

```

---
## 抽象建造者

```python
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass
```

---
## 具体建造者

隐藏内部结构

```python title="女人"
class SexGirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '好看的脸'

    def build_body(self):
        self.player.body = '瘦小'

    def build_arm(self):
        self.player.arm = '漂亮胳膊'

    def build_leg(self):
        self.player.leg = '大腿'
```

```python title="怪物"
class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '怪物的脸'

    def build_body(self):
        self.player.body = '大身体'

    def build_arm(self):
        self.player.arm = '可怕胳膊'

    def build_leg(self):
        self.player.leg = '可怕大腿'

```

---
## 控制者

控制顺序 可以对构建过程更精细的控制

```python
class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player
```


---
## 客户端

```python
builder = Monster()
director = PlayerDirector()
p = director.build_player(builder)
print(p)
```


