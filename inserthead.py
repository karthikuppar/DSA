class Solution:
    def insertAtHead(self, head, X):
        newnode=ListNode(X)
        newnode.next=head
        return newnode
    def printnext(self,head):
        current=head
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
newhead=(a.insertAtHead(head,7))
a.printnext(newhead)