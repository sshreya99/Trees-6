# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""
        result = []
        que = [root]
        while que:
            curr = que.pop(0)
            if curr:
                result.append(str(curr.val))
                que.append(curr.left)
                que.append(curr.right)
            else:
                result.append("None")
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return []
        nodes = data.split(",")
        print(nodes)
        root = TreeNode(nodes[0])
        que = [root]
        i = 1
        while que:
            curr = que.pop(0)

            if nodes[i] != "None":
                curr.left = TreeNode(nodes[i])
                que.append(curr.left)
            i += 1

            if nodes[i] != "None":
                curr.right = TreeNode(nodes[i])
                que.append(curr.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
