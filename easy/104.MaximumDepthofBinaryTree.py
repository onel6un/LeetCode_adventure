class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        """Определяет максимульную глубину бинарного дерева
        проходом в ширину"""
        if not root:
            return 0

        list_apex = [root]

        layer = 0
        while list_apex:
            layer += 1
            layer_apex = []
            for apex in list_apex:
                if apex.left:
                    layer_apex.append(apex.left)
                if apex.right:
                    layer_apex.append(apex.right)
            list_apex = layer_apex
        return layer
