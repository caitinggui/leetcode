# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-03-14 14:53
 * Description   :
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. 
'''


from Queue import PriorityQueue


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            # 把根节点放进去
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            curr.next = q.get()[1]  # 取出最小跟节点
            curr = curr.next
            # 放入最小节点的下个节点, 然后和之前已放入的对比
            if curr.next:
                q.put((curr.next.val, curr.next))
        return dummy.next

    def mergeKLists2(self, lists):
        values = []
        for root in lists:
            while root:
                values.append(root.val)
                root = root.next
        values.sort()
        node = root = ListNode(None)
        for value in values:
            node.next = ListNode(value)
            node = node.next
        return root.next
