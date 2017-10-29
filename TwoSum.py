#coding:utf-8

'''
   给出一个列表，已经一个给定值，计算出哪两位相加可以得到该给定值，eg：
   n = [1,4,7,3,2], target = 9,那么返回值为：[2,4] ------n[2] + n[4] == 9
   
   [0,3,4,0]--0, [3,2,4]--6
'''

def two_sum(n, target):
    dic = {}
    for i, x in enumerate(n):
        # 这里的in指的是dic中的键值，也就相当于 x in [target-xn]
        if x in dic:
            return [dic[x], i]
        else:
            dic[target-x] = i
            
            
# if i in range(len(n)):
    # if n[i] in dic:
    # ...