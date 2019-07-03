# 在运行时提供密码输入提示
# 当写脚本时，不是把密码固定到脚本中
# 默认会自动从shell环境中获取用户名和密码

import getpass

user = getpass.getuser()
passwd = getpass.getuser()

print(user,passwd)
# if svc_log(user,passwd):
#     print('Yay!')
# else:
#     print('Boo！')