# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(root.val)
            root.left = dfs(root.left)
            root.right = dfs(root.right)
        dfs(root)
        return ','.join(list(map(str, res)))
                
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # root = TreeNode(int(data[0]))
        data = data.split(',')
        self.i = 0
        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(data[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        root  = dfs()
        return root