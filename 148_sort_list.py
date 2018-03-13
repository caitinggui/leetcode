# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-03-13 11:55
 * Description   : Sort a linked list in O(n log n) time using constant space complexity.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        stack.sort()
        node = head
        i = 0
        while node:
            node.val = stack[i]
            node = node.next
            i += 1
        return head
