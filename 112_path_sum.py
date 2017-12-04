# coding: utf-8

'''
 Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
For example:
Given the below binary tree and sum = 22,
[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum_error(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        会判断树中是否有一串节点的值的和满足给定值，但不一定是到叶子节点
        题目是要求根到叶子节点
        """
        def helper(root, target):
            if not root:
                return target
            target = target - root.val
            # print root.val, target    # 供调试
            if target == 0:
                return target
            else:
                target = helper(root.left, target)
                if target == 0:
                    return target
                if root.left:
                    target += root.left.val
                target = helper(root.right, target)
            return target

        if not root:
            return False
        target = helper(root, sum)
        print target

        # import pdb; pdb.set_trace()
        return target == 0

    def hasPathSum_error2(self, root, sum):
        def helper(root, target):
            target -= root.val
            if not root.left and not root.right:
                result.append(target)
            print root.val, target
            if root.left:
                target = helper(root.left, target)
                # 从左子树到右子树时，要把减去的值加回去
            # if root.left:
                target += root.left.val
            if root.right:
                target = helper(root.right, target)
            return target

        if not root:
            return False
        result = []
        helper(root, sum)
        print result
        return 0 in result

    def hasPathSum2(self, root, sum):
        """正确的解法，但是效率太慢
        对递归的一些理解:递归的理解
        递归每一层有自己的栈，用来保存自己的值，每一层互不影响，除非要赋值，return也只是返回自己这层的变量，如果不赋值也是影响不了其他的层"""
        def helper(root, target):
            target += root.val
            if not root.left and not root.right:
                result.append(target)
            print root.val, target
            if root.left:
                target = helper(root.left, target)
                # 离开左子树后，和要减去左子树的值, 因为上面有target=helper(root.left, target), 也就是说本层的target被修改了
                # 如果没有target=helper(root.left, target), 那么可以不用target-=root.left.val, 就像下面的root.right的处理
                target -= root.left.val
            if root.right:
                helper(root.right, target)
                # target = helper(root.right, target)
                # target -= root.right.val  # 同左子树的处理
            return target

        if not root:
            return False
        result = []
        helper(root, 0)
        print result
        return sum in result

    def hasPathSum(self, root, sum):
        """总的思想就是计算出每一层每个节点的sum，如果是叶子节点就判断sum是否等于给定值"""
        def helper(root, sum_so_far, sum):
            if root:
                sum_so_far += root.val  # 此时，每个节点有个sum_so_far，不同的节点值不互相干扰
                print root.val, sum_so_far
                # 到了叶子节点就不再递归
                if not root.left and not root.right:
                    return sum_so_far == sum
                else:
                    return helper(root.left, sum_so_far, sum) or\
                        helper(root.right, sum_so_far, sum)
            return False
        return helper(root, 0, sum)


tree = TreeNode(5)
tree.left = TreeNode(4)
tree.right = TreeNode(8)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(1)
tree.left.left = TreeNode(11)
tree.right.right.right = TreeNode(1)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
s = Solution()
print s.hasPathSum(tree, 22)
print s.hasPathSum(None, 0)
assert(s.hasPathSum(tree, 22) is True)
assert(s.hasPathSum(None, 0) is False)
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
assert(s.hasPathSum(tree2, 1) is False)


def createTree(datas):
    """按照Leecode的格式创建树
    [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
    总的思想是，把已经初始化的节点加入nodes，然后一个个弹出，绑定子节点，
    此时，子节点也应继续加入nodes中. try是为了防止超出datas长度
    """
    root = TreeNode(datas[0])
    nodes = [root]
    datas_index = 1
    while nodes:
        node = nodes.pop(0)
        if not node:
            # 一个node对应两个子节点，如果node为空，说明接下来的子节点也可以舍弃
            datas_index += 2
            continue
        try:
            if datas[datas_index]:
                node.left = TreeNode(datas[datas_index])
            nodes.append(node.left)
            datas_index += 1
        except IndexError:
            pass
        try:
            if datas[datas_index]:
                node.right = TreeNode(datas[datas_index])
            nodes.append(node.right)
            datas_index += 1
        except IndexError:
            pass
    return root


datas = [1, -2, -3, 1, 3, -2, None, -1]
root = createTree(datas)
assert(s.hasPathSum(root, -4) is True)
