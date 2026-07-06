class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        p1=headA
        p2=headB
        while p1!=p2:
            if p1 is None:
                p1=headB
            else:
                p1=p1.next
            if p2 is None:
                p2=headA
            else:
                p2=p2.next
        return p1
    #def printList(self, head):
        current=head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)
node7=ListNode(7)
node8=ListNode(8)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node7.next=node8
node8.next=node4
headA=node1
headB=node7
a=Solution()
ans=a.getIntersectionNode(headA,headB)
print(ans.data)