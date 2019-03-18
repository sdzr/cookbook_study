#当希望在迭代或者其他形式的处理过程中，希望记录下最后处理的迭代记录的有限历史。
#采用colloctions.deque，是一个完美的应用场景

#example 1:
from collections import deque

#匹配一个文本，输出匹配到的文本，并输出最后处理过的5个记录。
def search(lines,pattern,history):
    previous_lines=deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield pattern,previous_lines
        previous_lines.append(line)

#当deque不指定长度时，可以得到一个无限的队列，而且队列可以从左边或者右边同时添加或删除
#与list相比，做插入操作时，deque的复杂度为O（1），而lsit为O（n）
#example 2:
q=deque()
q.append(1)
q.append(2)
q.append(3)
q.appendleft(10)
q.popleft()


if __name__=='__main__':
    with open('scpt1-3.txt',encoding='utf8') as f:
        for line,previous in search(f,'python',5):
            for pline in previous:
                print(pline,end=' ')
            print('_'*20)
