class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        current=head
        while current is not None:
            copy=ListNode(current.val)
            copy.next=current.next
            current.next=copy
            current=copy.next
        current=head
        while current is not None:
            if current.random is not None:
                current.next.random=current.random.next
            current=current.next.next
        current=head
        copyhead=head.next
        while current is not None:
            copy=current.next
            current.next=current.next.next
            if copy.next is not None:
                copy.next=copy.next.next
            current=current.next
        return copyhead
def printList(head):

    current = head

    while current is not None:

        if current.random is None:
            randomValue = "None"
        else:
            randomValue = current.random.val

        print("Node =", current.val
              ,
              " Random =", randomValue)

        current = current.next
class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node1.random = None
node2.random = node1
node3.random = node5
node4.random = node2
node5.random = node3
a=Solution()
head=node1
ans=a.copyRandomList(head)
printList(ans)



