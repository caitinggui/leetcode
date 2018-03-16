# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-03-16 18:04
 * Description   :
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.


Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """这里用了先跟序方法序列化的"""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        有些小瑕疵，没有返回string
        """
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            else:
                res.append(None)
        return res

    def deserialize(self, nodes):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not nodes:
            return
        val = nodes.pop(0)
        root = None
        # if val:
        if val is not None:
            root = TreeNode(val)
            root.left = self.deserialize(nodes)
            root.right = self.deserialize(nodes)
        return root


class Codec2:
    """这里用了层遍历方法序列化的"""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        stack = [root]
        res = []
        while stack:
            stack_len = len(stack)
            for _ in range(stack_len):
                node = stack.pop(0)
                if node:
                    res.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
                else:
                    res.append(None)
        return res

    def deserialize(self, nodes):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        pass


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

s = Codec()

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.left.left = TreeNode(4)
t1.left.right = TreeNode(5)
t1.left.right.left = TreeNode(8)
t1.right = TreeNode(3)
t1.right.left = TreeNode(6)
t1.right.right = TreeNode(7)
t1.right.right.left = TreeNode(9)
t1.right.right.right = TreeNode(10)

print(s.serialize(t1))

nodes = [1, 2, 4, None, None, 5, 8, None, None, None, 3, 6, None, None, 7, 9, None, None, 10, None, None]
print nodes
root = s.deserialize(nodes)
print(s.serialize(root))

nodes = [-1, 0, 1]
root = s.deserialize(nodes)
print(s.serialize(root))
