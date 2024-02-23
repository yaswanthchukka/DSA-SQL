# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res=ListNode()
        res1=[]
        res2=[]
        t1=l1
        while t1:
            res1.append(t1.val)
            t1=t1.next
        t2=l2
        while t2:
            res2.append(t2.val)
            t2=t2.next
        m=max(len(res1),len(res2))
        res1+=[0]*(m-len(res1))
        res2+=[0]*(m-len(res2))
        c=0
        k=res
        for i in range(m):
            t=(res1[i]+res2[i])+c
            k.next=ListNode(t%10)
            c=t//10
            k=k.next
        if c>0:
            k.next=ListNode(c)  
        return res.next
