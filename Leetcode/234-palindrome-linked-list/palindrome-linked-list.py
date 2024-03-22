# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        k=[]
        t=head
        while t:
            k.append(t.val)
            t=t.next
        if k==k[::-1]:
            return True
        return False

        