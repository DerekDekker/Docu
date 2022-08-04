from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine


# table 是否创建表
class 名称(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


# 是否 在数据库中创建表
table=False

# 主键
字段: Optional[int] = Field(default=None, primary_key=True)

# 可选可空
字段: Optional[int] = None

# 索引
字段: str = Field(index=True)

----------------------------------一对多关系
一对多
字段: Optional[int] = Field(default=None, foreign_key='表.主键')
    default=None  可以为空


可用于主键
名称2: List["外键SQLModel"] = Relationship(back_populates="名称3")
    # 名称2=[外键实例, 外键实例]  创建主键实例 或 修改主键实例 可以通过主键来创建外键关系
    # 主键实例.名称2.append(外键实例)  可以通过主键实例来创建外键关系
    # 可以直接以主键实例访问外键列表 主键SQLModel实例.名称2

可用于外键
名称3: Optional[主键SQLModel] = Relationship(back_populates="名称2")
    # 创建实例时可以只传 主键实例 而不是 主键实例.id
    # 可以直接以外键实例访问主键属性 外键SQLModel实例.名称3
    # 删除关系 外键SQLModel实例.名称3 = None

----------------------------------多对多关系
# 链接表
class HeroTeamLink(SQLModel, table=True):
    team_id: Optional[int] = Field(
        default=None, foreign_key="team.id", primary_key=True
    )
    hero_id: Optional[int] = Field(
        default=None, foreign_key="hero.id", primary_key=True
    )

class Team(SQLModel, table=True):
    # 字段

    heroes: List["Hero"] = Relationship(back_populates="teams", link_model=HeroTeamLink)

class Hero(SQLModel, table=True):
    # 字段

    teams: List[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)

# 创建多对多关系的数据
hero_deadpond = Hero(
    字段="值",
    字段2="值",
    teams=[Team实例, Team实例],
)

# 新增多对多
Team实例.heroes.append(hero_deadpond)

# 删除多对多
hero_deadpond.teams.remove(Team实例)

----------------------------------多对多关系 额外字段
class HeroTeamLink(SQLModel, table=True):
    team_id: Optional[int] = Field(
        default=None, foreign_key="team.id", primary_key=True
    )
    hero_id: Optional[int] = Field(
        default=None, foreign_key="hero.id", primary_key=True
    )
    # 额外字段
    is_training: bool = False

    # 额外设置
    team: "Team" = Relationship(back_populates="hero_links")
    hero: "Hero" = Relationship(back_populates="team_links")


class Team(SQLModel, table=True):
    # 字段

    hero_links: List[HeroTeamLink] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    #字段

    team_links: List[HeroTeamLink] = Relationship(back_populates="hero")


# 创建关系
deadpond_preventers_link = HeroTeamLink(team=Team实例, hero=Hero实例, is_training=True)

# 不知道啥玩意 创建关系可能是 需要提交 Team实例
Team实例.hero_links.append(deadpond_preventers_link)


----------------------------------仅在编辑代码时运行
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .hero_model import Hero

