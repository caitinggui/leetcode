# -*- coding: utf-8 -*-
'''
 * Author        : caitinggui
 * Email         : caitinggui@qq.com
 * Created time  : 2018-03-12 17:00
 * Description   :
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preOrder(root):
    """先根序遍历，先中后左再右"""
    if not root:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)


def preOrder2(root):
    '''先跟序遍历的非递归
    核心关键点就是用一个栈记录节点以及节点是否被访问，
    然后先思考节点没有被访问时的表现，
    再想想节点被访问的表现
    最终确定好节点在栈的位置
    '''
    stack = [(root, 0)]  # 0表示没被访问过
    while stack:
        node, visited = stack.pop()
        if not node:
            continue
        if visited:
            stack.append((node.right, 0))
        else:
            print(node.val)          # 先遍历中节点
            stack.append((node, 1))  # 这个节点已经遍历了，回栈，等待遍历右子树
            stack.append((node.left, 0))


def inOrder(root):
    """中根序遍历，先左后中再右"""
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)


def inOrder2(root):
    stack = [(root, 0)]
    while stack:
        node, visited = stack.pop()
        if not node:
            continue
        if visited:
            print(node.val)
            stack.append((node.right, 0))
        else:
            stack.append((node, 1))  # 节点已经访问过，但还没取值
            stack.append((node.left, 0))


def posOrder(root):
    """后根序遍历，先左后右再中"""
    if not root:
        return
    posOrder(root.left)
    posOrder(root.right)
    print(root.val)


def posOrder2(root):
    stack = [(root, 0)]
    while stack:
        node, visited = stack.pop()
        if not node:
            continue
        if visited:
            print(node.val)
        else:
            stack.append((node, 1))
            stack.append((node.right, 0))
            stack.append((node.left, 0))


def levelOrder(root):
    stack = [root]
    while stack:
        level = len(stack)
        for i in range(level):
            node = stack.pop(0)
            if not node:
                continue
            print(node.val)
            stack.append(node.left)
            stack.append(node.right)


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

# preOrder(t1)
# print([1, 2, 4, 5, 8, 3, 6, 7, 9, 10])
# preOrder2(t1)

# inOrder(t1)
# print([4, 2, 8, 5, 1, 6, 3, 9, 7, 10])
# inOrder2(t1)

# posOrder(t1)
# print([4, 8, 5, 2, 6, 9, 10, 7, 3, 1])
# posOrder2(t1)

levelOrder(t1)
