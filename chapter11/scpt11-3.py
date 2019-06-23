# 创建一个UDP服务器
from socketserver import UDPServer,BaseRequestHandler
import time

class TimeHanler(BaseRequestHandler):
    def handle(self):
        print('Got connect from',self.client_address)
        msg,sock=self.request
        resp=time.ctime()
        sock.sendto(resp.encode('ascii'),self.client_address)

if __name__=='__main__':
    serv=UDPServer(('',20000),TimeHanler)
    serv.serve_forever()