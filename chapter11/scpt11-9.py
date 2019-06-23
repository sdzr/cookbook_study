# 以简单方式验证客户端身份
# 验证方式，首先两边都知道密码
# 然后由服务其产生一个随机数，并发给客户端
# 客户端用随机数和密码hmac加密一下，生成一个字符串A，并发送给服务器
# 服务器用之前的随机数，和已知的密码hmac加密生成一个字符串B
# 如果A=B，那么则验证密码成功
# 但是并没有对数据进行加密

import hmac
import os

def client_authenticate(connection,scret_key):
    message = connection.recv(32)
    hash=hmac(scret_key,message)
    digest=hash.digest()
    connection.send(digest)

def server_authenticate(connection, scret_key):
    message = os.urandom(32)
    connection.send(message)
    hash = hmac(scret_key,message)
    digest=hash.digest()
    response=connection.recv(len(digest))
    return hmac.compare_digest(digest,response)

