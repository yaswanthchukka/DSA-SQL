# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        if t==None:
            return None
        l=ListNode(t.val)
        t=t.next
        while t:
            n=ListNode(t.val)
            n.next=l
            l=n
            t=t.next
        return l

        