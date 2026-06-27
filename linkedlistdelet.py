class Solution:
    def deleteHead(self, head):
        if head is None:
            return None
        head=head.next
        return head
    def printnext(self,newhead):
        current=newhead
        while current is not None:
            print(current.data,end=" ")
            current=current.next
class ListNode:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next
node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node1.next=node2
node2.next=node3
head=node1
a=Solution()
newhead=(a.deleteHead(head))
a.printnext(newhead)





