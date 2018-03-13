# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-03-13 12:07
 * Description   : 合并两个已排序的数组
'''


def mergeArray(nums_a, nums_b):
    """一个个扫描过去，然后处理还没扫完的"""
    a_ptr = 0
    b_ptr = 0
    nums = []
    while a_ptr < len(nums_a) and b_ptr < len(nums_b):
        if nums_a[a_ptr] < nums_b[b_ptr]:
            nums.append(nums_a[a_ptr])
            a_ptr += 1
        else:
            nums.append(nums_b[b_ptr])
            b_ptr += 1
    if a_ptr < len(nums_a):
        nums += nums_a[a_ptr:]
    else:
        nums += nums_b[b_ptr:]
    return nums


a = [1, 4, 8, 9]
b = [2, 3]
print(mergeArray(a, b), [1, 2, 3, 4, 8, 9])
a = [1, 4, 8, 9]
b = [2]
print(mergeArray(a, b), [1, 2, 4, 8, 9])
a = [1, 4, 8, 9]
b = [12]
print(mergeArray(a, b), [1, 4, 8, 9, 12])
