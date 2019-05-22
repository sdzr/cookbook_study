# 读二进制结构的数组
from struct import Struct

def write_record(records,format,f):
    record_struct = Struct(format)
    for record in records:
        f.write(record_struct.pack(*record))
        print(record_struct.pack(*record))

records = [(2,3,4),(3,4,5)]

with open('data.bin','wb') as f:
    write_record(records,'<idd',f)


def read_records(format, f):
    record_struct=Struct(format)
    chunks = iter(lambda:f.read(record_struct.size),b'')
    return (record_struct.unpack(chunk) for chunk in chunks)

