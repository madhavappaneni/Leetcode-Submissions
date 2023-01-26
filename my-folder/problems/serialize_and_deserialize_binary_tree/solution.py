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
        def serial(node, string):
            if node is None:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = serial(node.left, string)
                string = serial(node.right, string)
            return string
        return serial(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def deserial(l):
            if l[-1] == 'None':
               l.pop()
               return None
            else:
                root = TreeNode(l[-1])
                l.pop()
                root.left = deserial(l)
                root.right = deserial(l)
                return root
        l = data.split(',')[::-1]
        return deserial(l)




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))