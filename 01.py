def calc_avg():
    """流式计算平均值"""
    total, counter = 0, 0
    avg_value = 11
    while True:
        value = yield avg_value
        print(value)

        total, counter = total + value, counter + 1
        avg_value = total / counter


gen = calc_avg()
next(gen)
print(gen.send(10))
print(gen.send(20))
print(gen.send(30))