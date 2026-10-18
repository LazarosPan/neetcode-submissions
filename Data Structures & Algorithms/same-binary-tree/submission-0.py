# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        binary trees p,q
        true if equivalent
        same structure, same values
        one way is to append every node and value into a list/dict with the order we see them and then compare the two.
        but it can be faster if we compare at each step the two trees, we dont need to go until the end if the two 
        are different we can return false when we find a difference        
        """
        if p is None and q is None:
            return True
        if p is None or q is None:      # exactly one is None
            return False
        if p.val != q.val:
            return False
        return (
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right)
                )