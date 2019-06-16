# 将python源码分解为字节码

import dis
def countdown(n):
    while n > 0:
        print('T-minus',n)
        n-=1
    print('Blastoff!')

dis.dis(countdown)
