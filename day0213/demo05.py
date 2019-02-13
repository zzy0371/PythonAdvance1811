"""
生成器
"""

"列表生成式 很好用，但是有缺点，有多少个元素就需要开辟多的空间 "
l1 = [x for x in range(100000)]
# print(l1[100])
"生成器写法 对象多占内存跟元素个数无关"
"生成器不能使用下标,但是可以使用for循环和 next（生成器对象）"
"生成器后面数据根据前面数据推算出来"
""
l2 = (x for x in range(100000))
# print(next(l2),next(l2),next(l2),next(l2))
# print(l1.__sizeof__())
# print(l2.__sizeof__())

# for r in l1:
#     print(r)

for r in l2:
    print(r)
