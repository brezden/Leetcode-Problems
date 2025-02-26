from typing import Optional, List

class ListNode:
    def __init__(self, x=0):
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = baseNode = ListNode()

        while (list1 != None and list2 != None):
            if (list1.val > list2.val):
                current.next = list2
                current = current.next
                list2 = list2.next
            else:
                current.next = list1
                current = current.next
                list1 = list1.next

        # Edge Case if one of the lists has one value
        if list1 != None or list2 != None:
            if list1 != None:
                current.next = list1
            else:
                current.next = list2

        return baseNode.next

nodes: List[int] = [2,4]
head1 = ListNode(1)
head1.addNodes(nodes)

nodes: List[int] = [3,4]
head2 = ListNode(1)
head2.addNodes(nodes)

print(head1.printList(), head2.printList())

solution = Solution()
head = solution.mergeTwoLists(head1, head2)
print(head.printList())

