class Solution:
    def middleOfLinkedList(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
class ListNode:
    def __init__(self, data=0, next=None):
        self.data =data
        self.next = next
node1=ListNode(3)
node2=ListNode(8)
node3=ListNode(7)
node4=ListNode(1)
node5=ListNode(3)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
head=node1
a=Solution()
middel=(a.middleOfLinkedList(head))
print(middel.data)
