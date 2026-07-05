class Solution:
    def addTwoNumbers(self, linkedList1, linkedList2):
        dummy=ListNode(0)
        current=dummy
        carry=0
        while linkedList1 is not None or linkedList2 is not None or carry:
            sum=carry
            if linkedList1 is not None:
                sum+=linkedList1.data
                linkedList1=linkedList1.next
            if linkedList2 is not None:
                sum+=linkedList2.data
                linkedList2=linkedList2.next
            carry=sum//10
            newnode=ListNode(sum%10)
            current.next=newnode
            current=current.next
        return dummy.next
    def printList(self, head):
        current = head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
node1 = ListNode(5)
node2 = ListNode(4)
node1.next = node2
two_node1=ListNode(4)
a=Solution()
ans=a.addTwoNumbers(node1,two_node1)
a.printList(ans)


     