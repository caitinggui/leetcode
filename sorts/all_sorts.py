# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-04-25 18:11
 * Description   : 基本的排序算法
八大排序算法: 插入排序，希尔排序，选择排序，冒泡排序，快速排序，归并排序，堆排序，基数排序
'''
import random
import time
import math


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


def _merge(left, right):
    """合并"""
    l_pos, r_pos = 0, 0
    result = []
    while l_pos < len(left) and r_pos < len(right):
        if left[l_pos] < right[r_pos]:
            result.append(left[l_pos])
            l_pos += 1
        else:
            result.append(right[r_pos])
            r_pos += 1
    result += left[l_pos:]
    result += right[r_pos:]
    return result


def mergeSort(nums):
    """归并排序
    如果列表的长度是0或1，那么它已经有序。否则：
    未排序的部分平均划分为两个子序列。
    每个子序列，递归使用归并排序。
    合并两个子列表，使之整体有序。
    """
    if len(nums) <= 1:
        return nums
    mid = len(nums) / 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return _merge(left, right)


def heapSort(nums):
    """堆排序
    它是选择排序的一种。可以利用数组的特点快速定位指定索引的元素。堆分为大根堆和小根堆，是完全二叉树。大根堆的要求是
    每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。在数组的非降序排序中，需要使用的就是大根堆，因为根据
    大根堆的要求可知，最大的值一定在堆顶"""
    def siftDown(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and nums[child] < nums[child + 1]:
                child += 1
            if nums[root] < nums[child]:
                nums[root], nums[child] = nums[child], nums[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in xrange((len(nums) - 2) // 2, -1, -1):
        siftDown(start, len(nums) - 1)

    # 堆排序
    for end in xrange(len(nums) - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        siftDown(0, end - 1)
    return nums


def radixSort(nums, radix=10):
    """基数排序(按数字的位数来处理，没有区分是否负数，所以需要处理一下负数)
    属于“分配式排序”（distribution sort），又称“桶子法”（bucket sort）或bin sort，顾名思义，它是透过键值的部份资讯，
    将要排序的元素分配至某些“桶”中，藉以达到排序的作用，基数排序法是属于稳定性的排序，其时间复杂度为O (nlog(r)m)，
    其中r为所采取的基数，而m为堆数，在某些时候，基数排序法的效率高于其它的稳定性排序法。

    nums为整数列表，radix为基数, 这里只能适用于正整数,以后再研究
    还有个bug：会把nums清空
    """
    K = int(math.ceil(math.log(max(nums), radix)))
    bucket = [[] for _ in range(radix)]
    for num in range(1, K + 1):
        for j in nums:
            bucket[j / (radix**(num - 1)) % (radix**num)].append(j)
        del nums[:]
        for z in bucket:
            nums += z
            del z[:]
    return nums


times = 10    # 测试次数
length = 900    # 要排序的数组长度
# 侵入式的函数，会修改原数组信息
funcs_invaded = [insertSort, shellSort, selectionSort, bubbleSort, bubbleSortImprove, quickSort, heapSort]
# 非侵入式函数，不修改原数组信息
funcs_not_invaded = [mergeSort, sorted]

# 准备数组
all_nums = []
for i in range(times):
    # 列表长度为length，数值从-length到length
    nums_org = [random.randint(-length, length) for _ in range(length)]
    tmp_nums = nums_org[:]
    all_nums.append((nums_org, sorted(tmp_nums)))

for func in funcs_invaded:
    time_start = time.time()
    for nums, answer in all_nums:
        tmp_nums = nums[:]  # 因为排序会改变数组内的顺序，所以要先复制出来
        tmp_nums_merge = func(tmp_nums)
        try:
            assert(tmp_nums == answer)
        except Exception:
            print("%s result error: %s\n expect: %s" % (func.func_name, nums, answer))
    print(func.func_name, " cost %0.4f" % (time.time() - time_start))


for func in funcs_not_invaded:
    time_start = time.time()
    for nums, answer in all_nums:
        tmp_nums = func(nums)
        try:
            assert(tmp_nums == answer)
        except Exception:
            print("%s result error: %s\n expect: %s" % (func.func_name, nums, answer))
    print(func, " cost %0.4f" % (time.time() - time_start))


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
