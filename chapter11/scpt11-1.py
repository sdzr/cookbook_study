# 以客户端的形式与客户端进行交互
from urllib import request,parse

url = 'https://blog.csdn.net/'

parms = {
    'name1':'value1',
    'name2':'value2'
}

querysting=parse.urlencode(parms)
print(querysting)
u = request.urlopen(url+'?'+querysting)

resp=u.read()
print(resp)


url1 = 'http://httpbin.org/post'
u1= request.urlopen(url1,querysting.encode('ascii'))
print(u1.read())


