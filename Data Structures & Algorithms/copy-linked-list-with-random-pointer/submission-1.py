"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        Map = { None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            Map[curr] = copy
            curr = curr.next
        # print(head)
        # print(Map)
        curr = head
        while curr:
            copy = Map[curr]
            copy.next = Map[curr.next]
            copy.random = Map[curr.random]
            curr = curr.next

        return Map[head]