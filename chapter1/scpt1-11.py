record='......100.......513.23....'

SHARES=slice(6,9)
PRICE=slice(16,22)

print(record[SHARES],record[PRICE])
#可以看到，slice(x,y) 函数是一个切片的别名，便于记住某一个固定的切片范围。