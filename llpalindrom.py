class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is  None:
            return True
        slow=head
        fast=head
        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow.next
        while current is not None:
            newnode=current.next
            current.next=prev
            prev=current
            current=newnode
        first=head
        second=prev
        while second is not None:
            if first.data!=second.data:
                return False
            first=first.next
            second=second.next
        return True
class ListNode:
    def __init__(self, data=0, next=None):
        self.data =data
        self.next = next
node1=ListNode(3)
node2=ListNode(7)
node3=ListNode(5)
node4=ListNode(7)
node5=ListNode(3)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
head=node1
a=Solution()
print(a.isPalindrome(head))
    

         



        
        