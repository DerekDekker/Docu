# SQLModel与FaseAPI

## 模型

### 基础模型

用于其他类继承, 一般不参与反序列化的字段不添加, 需要保密的字段不添加.

```python
class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
```

### 数据库模型

进行数据库修改, 可以添加额外字段

```python
class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
```

### 反序列化模型

反序列化, 对数据库进行操作
```python
class HeroCreate(HeroBase):
    pass
```

### 序列化模型

不对数据库进行操作

```python
class HeroRead(HeroBase):
    id: int
```

### 更新模型

用于更新, 所有字段都是可选到

```python
class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
```

---
## 创建

```python
@app.post("/heroes/", response_model=Hero)
def create_hero(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero
```

---
## 多个模型

多个 SQLModel模型 分开创建 读取 数据库模型

```python
@app.post("/heroes/", response_model=HeroRead)
def create_hero(hero: HeroCreate):
    with Session(engine) as session:
        # 从一个 SQLModel模型 对象复制数据到另一个 SQLModel模型
        db_hero = Hero.from_orm(hero)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero
```

---
## 查询

```python
@app.get("/heroes/")
def read_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes
```

---
## 分页

```python
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


@app.get("/heroes/", response_model=List[HeroRead])
def read_heroes(offset: int = 0, limit: int = Query(default=100, lte=100)):
    with Session(engine) as session:
        heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
        return heroes
```

---
## 更新

```python
@app.patch("/heroes/{hero_id}", response_model=HeroRead)
def update_hero(hero_id: int, hero: HeroUpdate):
    with Session(engine) as session:
        db_hero = session.get(Hero, hero_id)
        if not db_hero:
            raise HTTPException(status_code=404, detail="Hero not found")
        # 获取字典
        hero_data = hero.dict(exclude_unset=True)
        # 遍历全部字典 更新每个值
        for key, value in hero_data.items():
            setattr(db_hero, key, value)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)
        return db_hero
```

---
## 依赖注入

```python
from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


# 依赖函数
def get_session():
    with Session(engine) as session:
        yield session


@app.post("/heroes/", response_model=HeroRead)
def create_hero(*, session: Session = Depends(get_session), hero: HeroCreate):
    db_hero = Hero.from_orm(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero
```












