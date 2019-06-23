# 发送和接收大型数组
# 通过网络发送和接收大型数组，其中数据都是连续的，并且尽可能的少拷贝
# 充分利用内存覆盖，数组A发送到数组B，直接采用切片覆盖
# memeroyview内存覆盖

def send_from(arr,dest):
    view = memoryview(arr).cast('B')
    #  A的切片发送
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]

def recv_into(arr,source):
    view = memoryview(arr).cast('B')
    while len(view):
        nrecv=source.recv_into(view)
        view = view[nrecv:]

