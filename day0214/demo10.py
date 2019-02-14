"""
最终装饰是语法格式
"""

def checkuser(fun):
    def check():
        username = input("请输入用户名")
        if username == "wzk":
            fun()
        else:
            print("未授权")
    return check
@checkuser
def showlist():
    print("展示订单列表")

showlist()
