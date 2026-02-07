# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        i, j = headA, headB
        while i != j:
            if i.next == None and j.next == None:
                return None
            if i.next == None:
                i = headB
            else:
                i = i.next
            if j.next == None:
                j = headA
            else:
                j = j.next
        return i