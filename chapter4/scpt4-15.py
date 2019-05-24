# 合并多个有序序列，在对整个有序序列进行迭代
# 只是比较两个序列中第一个元素，将小的那个送出去
# 所以要想得到有序的返回，输入的序列必须是先排序好的，否则会的到错误的返回结果，而这一切是没有报错的。
import heapq

a =[1,4,7,9]
b = [2,5,6,11]

# 对所提供的序列不会一次性提取。所以可以处理很长的序列
for c in heapq.merge(a,b):
    print(c)


# 打开三个文件，排序
with open('sorted_file1', 'rt') as file1,\
    open('sorted_file2', 'rt') as file2,\
    open('merge_file','wt') as outof:
    for line in heapq.merge(file1,file2):
        outof.write(line)