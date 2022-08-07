import re

phone = "2004a959a559"

# 删除字符串中的 Python注释
# 删除非数字(-)的字符串
num = re.findall(r'A', phone, re.I)
# num = re.split(r'A', phone,)
print( num)
