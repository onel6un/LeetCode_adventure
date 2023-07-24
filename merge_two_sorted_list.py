from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    head = None
    tail = None

    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]):
        """Получает на вход два отсортированных в порядке возростания
        связанных списка, возвращает соединеный связанный список в порядке
        возрастания"""

        if (self._check_empty(list1) and self._check_empty(list2)):
            return None

        node1 = list1
        node2 = list2

        while node1 and node2:
            val1 = node1.val
            val2 = node2.val

            if node2.next and val1 > node2.next.val:
                self._push_back(val2)
                node2 = node2.next
                continue

            if node1.next and val2 > node1.next.val:
                self._push_back(val1)
                node1 = node1.next
                continue

            if val1 < val2:
                self._push_back(val1)
                self._push_back(val2)
            else:
                self._push_back(val2)
                self._push_back(val1)

            node1 = node1.next
            node2 = node2.next

        if self._check_empty(node1) and not self._check_empty(node2):
            self._contaminate_nodes(node2)

        if self._check_empty(node2) and not self._check_empty(node1):
            self._contaminate_nodes(node1)

        return self.head

    @staticmethod
    def _check_empty(list):
        return list is None

    def _contaminate_nodes(self, nodes):
        if not self.head:
            self.head = nodes
            return
        self.tail.next = nodes

    def _push_back(self, value):
        if not self.head:
            self.head = ListNode(val=value)
            self.tail = self.head
            return
        new_node = ListNode(val=value)
        self.tail.next = new_node
        self.tail = new_node
