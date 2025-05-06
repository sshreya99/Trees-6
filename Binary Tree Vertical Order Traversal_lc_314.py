# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = [(root, 0)]
        minVal = float("inf")
        maxVal = float("-inf")
        result = []
        dic = defaultdict(list)

        while que:
            curr, index = que.pop(0)
            minVal = min(minVal, index)
            maxVal = max(maxVal, index)
            dic[index].append(curr.val)
            if curr.left:
                que.append((curr.left, index - 1))
            if curr.right:
                que.append((curr.right, index + 1))
        
        for i in range(minVal, maxVal + 1):
            result.append(dic[i])
         
        return result
