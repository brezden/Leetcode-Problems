from typing import List, Optional

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        savedNode = None

        while head != None:
            nextNode = head.next
            head.next = savedNode
            savedNode = head
            head = nextNode

        return savedNode

nodes: List[int] = [2,3,4,5]
head = ListNode(1)
head.addNodes(nodes)

solution = Solution()
head.printList()
head = solution.reverseList(head)
head.printList()
