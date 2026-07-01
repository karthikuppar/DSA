class Solution:
    def reverseList(self, head):
        prev=None
        current=head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        return prev
    def newcode(self,head):
        current=head
        while current is not None:
            print(current.data,end=(" "))
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
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
head=node1
a=Solution()
newhead=a.reverseList(head)
a.newcode(newhead)


