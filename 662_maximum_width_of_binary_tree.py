# coding: utf-8

'''
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer. 
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def widthOfBinaryTree_error(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [root]
        max_size = 1
        while stack:
            size = len(stack)
            if_begin = True
            for i in range(size):
                node = stack.pop(0)
                if node:
                    stack.append(node.left)
                    stack.append(node.right)
                    if_begin = False
                elif not if_begin:
                    stack += [None, None]
            for node in stack[::-1]:
                if not node:
                    stack.pop()
                else:
                    break
            if max_size < len(stack):
                max_size = len(stack)
        return max_size

    def widthOfBinaryTree2(self, root):
        """其实可以不用记录depth"""
        if not root:
            return 0
        stack = [(root, 0, 0)]
        max_size = 1
        while stack:
            size = stack[-1][2] - stack[0][2] + 1
            if max_size < size:
                max_size = size
            size = len(stack)
            for _ in range(size):
                node, depth, pos = stack.pop(0)
                # print node.val, depth, pos
                if node.left:
                    stack.append((node.left, depth + 1, pos * 2))
                if node.right:
                    stack.append((node.right, depth + 1, pos * 2 + 1))
        return max_size

    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        stack = [(root, 0)]  # pos用来记录在该层的位置
        max_size = 0
        while stack:
            tree_size = stack[-1][1] - stack[0][1] + 1  # 记住要加1
            if max_size < tree_size:
                max_size = tree_size
            size = len(stack)
            for _ in xrange(size):
                node, pos = stack.pop(0)
                # print node.val, pos
                if node.left:
                    stack.append((node.left, pos * 2))
                if node.right:
                    stack.append((node.right, pos * 2 + 1))
        return max_size


s = Solution()

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.left = TreeNode(4)
print s.widthOfBinaryTree(t1)
assert(s.widthOfBinaryTree(t1) == 2)

t1.right.right = TreeNode(5)
print s.widthOfBinaryTree(t1)
assert(s.widthOfBinaryTree(t1) == 4)

t2 = TreeNode(1)
t2.right = TreeNode(2)
assert(s.widthOfBinaryTree(t2) == 1)
