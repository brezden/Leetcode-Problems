from typing import List

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
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

nodes: List[int] = [5,1,9]
head = ListNode(4)
head.addNodes(nodes)

solution = Solution()
head.printList()
solution.deleteNode(head.next)
head.printList()
