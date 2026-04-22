# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not q and not p:
            return True
        elif q and not p or not q and p:
            return False

        p_q = deque([p])
        q_q = deque([q])



        while p_q or q_q:
            if not q_q: 
                return False
            
            if not p_q:
                return False

            p_node = p_q.popleft()
            q_node = q_q.popleft()

            if p_node.val != q_node.val:
                return False
            
            if p_node.right and not q_node.right or p_node.left and not q_node.left:
                return False

            if p_node.left:
                p_q.append(p_node.left)
            
            if p_node.right:
                p_q.append(p_node.right)
            
            if q_node.left:
                q_q.append(q_node.left)
            
            if q_node.right:
                q_q.append(q_node.right)


        return  len(p_q) == 0 and len(q_q) == 0

        