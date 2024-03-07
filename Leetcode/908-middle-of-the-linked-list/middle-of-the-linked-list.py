# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        add=[]
        t=head
        while t:
            l.append(t.val)
            add.append(t)
            t=t.next
        k=len(l)
        if k%2!=0:
            return add[k//2]
        return add[(k+1)//2]
        # t2=head 
        # c=0
        # while t2:
        #     if c==(k//2):
        #         break
        #     c+=1
        #     t2=t2.next
        # return t2
        