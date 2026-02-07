"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        l = []
        if not root:
            return l
        for i in root.children:
            l.extend(self.postorder(i))
        l.append(root.val)
        return l