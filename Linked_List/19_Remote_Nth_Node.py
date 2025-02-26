from typing import Optional, List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        temp = []
        currentNode = self

        while (currentNode != None):
            temp.append(currentNode.val)
            currentNode = currentNode.next

        print(temp)

    def addNodes(self, nodes: List[int]):
        currentNode = self

        for node in nodes:
            newNode = ListNode(node)

            currentNode.next = newNode
            currentNode = newNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        result = ListNode(0)
        result.next = head
        dummy = result

        for i in range(n):
            head = head.next

        while head:
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next

        return result.next

nodes: List[int] = [2,3,4,5]
head = ListNode(1)
head.addNodes(nodes)

print(head.printList())
solution = Solution()
solution.removeNthFromEnd(head, 2)
print(head.printList())

