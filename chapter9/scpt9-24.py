# 解析并分析Python源码

import ast
top = ast.parse('for i in range(10):print(i)',mode='exec')
print(top)
print(ast.dump(top))
exec(compile(top,'<stdin>','exec'))