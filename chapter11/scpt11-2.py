# 创建一个tcp服务器

from socketserver import BaseRequestHandler,TCPServer,StreamRequestHandler,ThreadingTCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from',self.client_address)
        while True:
            msg=self.request.recv(8192)
            if not msg:
                print('not msg')
                break
            self.request.send(msg)

class EchoHandler1(StreamRequestHandler):
    def handle(self):
        print('Got connection from',self.client_address)
        for line in self.rfile:
            print(line)
            self.wfile.write(line)



if __name__=='__main__':
    serv =ThreadingTCPServer(('',2000),EchoHandler1)
    serv.serve_forever()