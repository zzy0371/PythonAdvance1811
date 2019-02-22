"""
正则表达式
"""
import re
# print(dir(re))
# pattern = "py1811"
# restr = "py1811hellopy1811     hi py1811"
# result = re.match(pattern,restr)
# result = re.search(pattern,restr)
# result = re.fullmatch(pattern,restr)
# print(result.group())
# result = re.findall(pattern,restr)
# result = re.split(pattern,restr)

# result = re.sub(pattern,"python1811",restr,2)

# result = re.finditer(pattern,restr)
# print(result)
# for r in result:
#     print(r.group())

# print(result)

# pattern = re.compile("py1811")
# result = pattern.findall(restr)
# print(result)



"""
得到Match对象可以使用group方法
match从头匹配
search匹配第一个
fullmatch从头匹配到尾

finditer 返回迭代器，迭代器中每一个元素都是Math对象都有group方法

得到列表列表项
findall 可以匹配到所有内容
split 使用正则切割字符串

返回字符串
sub 用新字符替换能够被正则匹配到的内容


compile可以得到一个pattern模型 进而通过模型调用响应方法

"""


# result = re.findall("\W","Py({[181 1he5ll oP\tY1.8+*11")
# print(result)

"""
re.I 忽略大小写
re.S 单行模式，在单行模式下 .符号可以匹配\n
"""


""" 8
.可以匹配任意字符
[]可以匹配其中一个 -代表范围
\d 数字  \D非数字
\s 空格或制表符 \S非空格.制表符
\w 匹配字母[0-9a-zA-Z]     \W匹配非字母
"""

".*?"

result = re.findall("\Wello", "hello aello5ello_ello .ello ^ello")
print(result)