class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        copy={}
        current=head
        while current is not None:
            copy[current]=Listnode(current.data)
            current=current.next
        current=head
        while current is not None:
            if current.next is not None:
                copy[current].next=copy[current.next]
            if current.random is not None:
                  copy[current].random=copy[current.random]
            current=current.next
        return copy[head]
class printlist(head):
    current=head 
    while current is not None:
        if current.random is None:
            return "None"
        else:
            randomvalue=current.random.data
        print(current.data,randomvalue)
        current=current.next
class ListNode:
    def __init__(self, data=0, next=None, random=None):
        self.data = data
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
printlist(ans)



