# coding: utf-8

'''
Given two binary tree1s and imagine that when you put one of them to cover the other, some nodes of the two tree1s are overlapped while the others are not.

You need to merge them into a new binary tree1. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree1.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree1:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
Note: The merging process must start from the root nodes of both tree1s.
'''


# Definition for a binary tree1 node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """这里有个隐患，因为合并后的t1包含t2的节点，后面如果t2的数据被修改，t1也会被修改
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        root = t1
        stack1 = [t1]
        stack2 = [t2]
        while stack1 or stack2:
            t1 = stack1.pop()
            t2 = stack2.pop()
            t1.val += t2.val
            if t2.right:
                if t1.right:
                    stack1.append(t1.right)
                    stack2.append(t2.right)
                else:
                    t1.right = t2.right    # 把t2的节点给t1
            if t2.left:
                if t1.left:
                    stack1.append(t1.left)
                    stack2.append(t2.left)
                else:
                    t1.left = t2.left
        return root

    def mergeTrees(self, t1, t2):
        """递归方法,也是在t1的基础上合并t2，没有创建新树，有隐患"""
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t2.right = self.mergeTrees(t2.right, t2.right)
        return t1

    def mergeTrees(self, t1, t2):
        if not t1:
            return t2
        if not t2:
            return t1
        t = TreeNode(t1.val + t2.val)
        t.left = self.mergeTrees(t1.left, t2.left)
        t.right = self.mergeTrees(t1.right, t2.right)
        return t

    def show(self, root):
        if not root:
            return
        print root.val
        self.show(root.left)
        self.show(root.right)


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)
tree2.left.right = TreeNode(4)
tree2.right.left = TreeNode(5)
tree2.right.right = TreeNode(6)
s = Solution()

root = s.mergeTrees(tree1, tree2)
print "----tree1----"
s.show(tree1)
print "----tree2----"
s.show(tree2)
