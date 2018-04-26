# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-04-25 18:11
 * Description   : 所有基本的排序算法
'''
import random
import time


def insertSort(nums):
    """插入排序
    从第一个元素开始，该元素可以认为已经被排序
    取出下一个元素，在已经排序的元素序列中从后向前扫描
    如果该元素（已排序）大于新元素，将该元素移到下一位置
    重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
    将新元素插入到该位置后
    重复步骤2~5
    """
    for i in range(len(nums)):
        key = nums[i]
        j = i
        # 从后往前扫，发现大数，就把大数往后挪一位
        while j > 0 and nums[j - 1] > key:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = key


def shellSort(nums):
    """希尔排序
    也称递减增量排序算法，是插入排序的一种高速而稳定的改进版本。
    希尔排序是基于插入排序的以下两点性质而提出改进方法的：
        1、插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
        2、但插入排序一般来说是低效的， 因为插入排序每次只能将数据移动一位
    """
    gap = len(nums) / 2
    while gap > 0:
        # 一组一组是从后往前扫，就是插入排序方式
        for i in range(gap, len(nums)):
            key = nums[i]
            j = i
            while j >= gap and nums[j - gap] > key:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = key
        gap = gap / 2


def selectionSort(nums):
    """选择排序法
    第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；
    第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
    以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，
    使有序序列不断增长直到全部排序完毕。
    """
    for i in range(len(nums)):
        min_index = i    # 记录出现最小值的那个索引
        for j in range(i + 1, len(nums)):  # 从i的下一位开始
            if nums[j] < nums[min_index]:
                min_index = j    # 更新最小值的索引
        nums[i], nums[min_index] = nums[min_index], nums[i]  # 将最小值提到最前面


def bubbleSort(nums):
    """冒泡排序
    比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    针对所有的元素重复以上的步骤，除了最后一个。
    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    """
    # 每轮走下来，最后一个数就是最大的数
    for i in range(len(nums)):
        # 不用对比已经排好的数，所以len(nums) - i
        for j in range(1, len(nums) - i):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]


def bubbleSortImprove(nums):
    """改进的冒泡排序
    用一个标志位记录这轮有没有发生交换，没有交换表示全部有序了
    """
    for i in range(len(nums)):
        exchange = False
        for j in range(1, len(nums) - i):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                exchange = True
        if not exchange:
            break


def __quickSort(nums, left, right):
    """快排的单次排序"""
    key = nums[left]
    while left < right:
        while right > left:
            if nums[right] < key:
                nums[left] = nums[right]
                left += 1
                break
            right -= 1
        while left < right:
            if nums[left] > key:
                nums[right] = nums[left]
                right -= 1  # 这步不能漏了
                break
            left += 1
    nums[left] = key
    return left


def _quickSort(nums, left, right):
    """快排的封装
    从数列中挑出一个元素，称为 “基准”（pivot），
    重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
    递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
"""
    if left < right:
        mid = __quickSort(nums, left, right)
        _quickSort(nums, left, mid - 1)
        _quickSort(nums, mid + 1, right)


def quickSort(nums):
    """快速排序法
    """
    _quickSort(nums, 0, len(nums) - 1)


def heapSort(nums):
    """堆排序"""
    pass


times = 20    # 测试次数
length = 800    # 要排序的数组长度
funcs = [insertSort, shellSort, selectionSort, bubbleSort, bubbleSortImprove, quickSort]
# 准备数组
all_nums = []
for i in range(times):
    # 列表长度为length，数值从-100到100
    nums_org = [random.randint(-100, 100) for _ in range(length)]
    tmp_nums = nums_org[:]
    all_nums.append((nums_org, sorted(tmp_nums)))

for func in funcs:
    time_start = time.time()
    for nums, answer in all_nums:
        tmp_nums = nums[:]  # 因为排序会改变数组内的顺序，所以要先复制出来
        func(tmp_nums)
        try:
            assert(tmp_nums == answer)
        except Exception:
            print("%s result error: %s\n expect: %s" % (func.func_name, nums, answer))
    print(func.func_name + " cost %0.4f" % (time.time() - time_start))


def insertSortError(nums):
    """插入排序的错误实现，交换太多了
    """
    for i in range(len(nums) - 1):
        j = i + 1
        while j > 0:
            # 从后往前扫，发现大数，就把大数往后挪一位
            if nums[j] < nums[j - 1]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1


def shellSortError(nums):
    """希尔排序的错误实现，交换太多了
    """
    gap = len(nums) / 2
    while gap > 0:
        # 一组一组是从后往前扫，就是插入排序方式
        for i in range(gap, len(nums)):
            j = i - gap
            while j >= 0:
                if nums[j + gap] < nums[j]:
                    nums[j], nums[j + gap] = nums[j + gap], nums[j]
                j -= gap
        gap = gap / 2
