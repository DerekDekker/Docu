-------------------------------------------------字符串
# 保存
r.set(键, 值)
    ex=1 过期秒
    px=1 过期毫秒
    nx=False  是否 键不存在时才执行
    xx=False  是否 只有键存在时才执行

# 追加内容
r.append(键, 值)

# 获取
r.get(键)
r[键]
r.mget(键, 键)  # 获取多个键


=======================HASH
# 增加 如果存在则修改
r.hset(键, HASH键, 值)

# 只能创建
r.hsetnx(键, HASH键, 值)

# 获取 键 所有 HASH键
r.hkeys(键)

# 获取 单个值
r.hget(键, HASH键)

# 获取 多个值
r.hmget(键, HASH键, HASH键)

# 获取全部键值 返回字典 dick
r.hgetall(键)

# 获取 键值对的个数
r.hlen(键)

# 获得 所有键
r.hkeys(键)

# 获得 所有值
r.hvals(键)

# 判断 HASH键 是否存在
r.hexists(键, HASH键)

# 删除
r.hdel(键, HASH键)

# 自增 递减
r.hincrby(键, HASH键, amount=1)  # 自增
r.hincrby(键, HASH键, amount=-1)  # 递减

# 自增 递减 浮点数
r.hincrbyfloat(键, HASH键, amount=1.0)  # 自增
r.hincrbyfloat(键, HASH键, amount=-1.0)  # 递减

# 返回可迭代对象
r.hscan_iter(键)

-------------------------------------------------list
# 新增
r.lpush(键, 值, 值, 值)  # 从左边新增加 开始处
r.rpush(键, 值, 值, 值) # 从右边新增加 结尾处

# 索引取值
r.lindex(键, 0)

# 切片获取
r.lrange(键, 0, -1)

# 列表长度
r.llen(键)

# 修改
r.lset(键, 索引, 值)

# 删除
r.lrem(键, num, 值)
    num=0  删除数量 0 代表全部

# 弹出第一个值 并返回
r.lpop(键)  # 左边
r.rpop(键)  # 右边

# 一个列表移到另一个列表
r.rpoplpush(键1, 键2)


-------------------------------------------------set 集合
# 新增
r.sadd(键1, 值, 值, 值, 值)

# 获取全部成员
r.smembers(键1)

# 获取个数
r.scard(键1)

-------------------------------------------------自增 递减
# 自增值
r.incr(键)  # 整数
    amount=1  每次增加的数量

r.incrbyfloat(键)  # 浮点数
    amount=1.1  每次增加的数量

# 递减
r.decr("foo", amount=1)
