# 序列化python对象
# 由于涉及到安全性，一般涉及到外部系统的对象都不能使用pickle
# 因为load反序列化的对象可能会被人伪造出来
import pickle

data = r'fasfasdgaasdf第三方'
f = open('tmp','wb')
pickle.dump([1,3,4],f)
pickle.dump('hello',f)
f.close()

with  open('tmp','rb') as f:
    d= pickle.load(f)
    print(d)
    print(pickle.load(f))

# pickle 可以记录某种系统状态，比如load后，程序继续运行

# 对于大型数据结构，pickle性能较差
# 由于pickle和python关联太紧密，一旦源码改变，数据将难以读取，不适合长期保存数据
# 应该使用更加标准的数据编码，比如xml，CSV，JSON（他们支持的语言多，便于源码的修改）

