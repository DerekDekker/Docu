from pydantic import BaseModel, ValidationError, constr


----------------模型
class 名称(BaseModel):
    # 字段
    名称: 类型
    名称: 类型 = Field(..., example="Foo")  example 例子

    class Config:
        # 是否 ORM 模型绑定
        orm_mode = True

        # 额外字段
        schema_extra = {
            # 例子
            'example': {
                'name': '小王',
            },
        }

继承
class 名称(其他BaseModel类):
    pass

----------------实例化
名称 = BaseModel类(**字典, 字段=值)

拷贝BaseModel对象
名称 = BaseModel对象.copy(update=字典)
    update 更新字段值

----------------类型
from pydantic import HttpUrl
from datetime import datetime

HttpUrl  URL链接
datetime  时间

----------------解析
from fastapi.encoders import jsonable_encoder


BaseModel对象.dict()  # 转 字典
    exclude_unset=False  是否 排除未传
BaseModel对象.json()  # 转 Json
BaseModel类.parse_obj(obj=字典)  # 字典 转 BaseModel类实例
BaseModel类.parse_raw('{"id": 123, "name": "John Snow"}')  # 原始数据 转 BaseModel类实例
jsonable_encoder(BaseModel对象)  转换为适配 JSON 的数据类型


----------------操作
BaseModel类实例.属性

----------------ORM
BaseModel类.from_orm(ORM实例)

----------------字段验证
from pydantic import Field

名称: str = Field(..., example='BeiJing')

...         也可以换成默认值
ge          最小值 int
le          最大值 int
min_length  最小长度 str
max_length  最大长度 str
default     默认值
example     例子
title       标题
description 描述
更多





