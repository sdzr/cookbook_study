# 调用父类中的方法

class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()
b=B()
b.spam()
