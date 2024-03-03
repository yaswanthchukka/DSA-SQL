# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        k=head
        c=0
        if k.next==None:
            head=None
            return head
        while k:
            c+=1
            k=k.next
        t=head
        a=c-n
        if c==n:
            q=head.next
            head.next=None
            head=q
        b=0
        while t:
            if b==a-1:
                t1=t.next.next
                t.next.next=None
                t.next=t1
            b+=1
            t=t.next
        return head
        