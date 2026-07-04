class Solution:
    def deleteNode(self, node):
        node.data=node.next.data
        node.next=node.next.next

    def printList(self, head):
        current = head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(9)
node1.next = node2
node2.next = node3
node3.next = node4
head =node1
a=Solution()
a.deleteNode(node2)
a.printList(head)