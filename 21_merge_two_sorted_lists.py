# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-03-14 11:43
 * Description   :
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists_slow(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        生成的链是全新的
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            root = ListNode(l1.val)
            l1 = l1.next
        else:
            root = ListNode(l2.val)
            l2 = l2.next
        node = root
        while l1 and l2:
            if l1.val < l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                l2 = l2.next
            node = node.next
        while l1:
            node.next = ListNode(l1.val)
            node = node.next
            l1 = l1.next
        while l2:
            node.next = ListNode(l2.val)
            node = node.next
            l2 = l2.next
        return root

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        # 第一个节点可以废弃，这样省的初始化处理
        curr = head = ListNode(-1)
        while (l1 and l2):
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        return head.next


def pprint(node):
    while node:
        print(node.val)
        node = node.next


s = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

root = s.mergeTwoLists(l1, l2)
pprint(root)
