"""Week 3 homework: The Royal Rail Ledger.

Implement the required functions below.
Use stdlib only.
"""

from __future__ import annotations


class SLLNode:
    """Node for a singly linked list."""

    def __init__(self, value: int, next: "SLLNode | None" = None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    """Simple singly linked list with a head reference."""

    def __init__(self) -> None:
        self.head: SLLNode | None = None


class DLLNode:
    """Node for a doubly linked list."""

    def __init__(
        self,
        value: int,
        prev: "DLLNode | None" = None,
        next: "DLLNode | None" = None,
    ) -> None:
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """Simple doubly linked list with head and tail references."""

    def __init__(self) -> None:
        self.head: DLLNode | None = None
        self.tail: DLLNode | None = None


def build_sll_from_list(values: list[int]) -> SinglyLinkedList:
    sll = SinglyLinkedList()

    if len(values) == 0:
        return sll

    sll.head = SLLNode(values[0])
    current = sll.head

    for i in range(1, len(values)):
        new_node = SLLNode(values[i])
        current.next = new_node
        current = new_node

    return sll


def sll_to_list(sll: SinglyLinkedList) -> list[int]:
    result = []
    current = sll.head

    while current != None:
        result.append(current.value)
        current = current.next

    return result



def find_first_repeat_sll(sll: SinglyLinkedList) -> int | None:
    seen = []
    current = sll.head

    while current != None:
        if current.value in seen:
            return current.value
        else:
            seen.append(current.value)

        current = current.next

    return None



def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    current = dll.head

    while current != None:
        next_node = current.next
        if current.value == target:

            if current.prev == None:
                dll.head = current.next
                if dll.head != None:
                    dll.head.prev = None


            elif current.next == None:
                dll.tail = current.prev
                if dll.tail != None:
                    dll.tail.next = None


            else:
                current.prev.next = current.next
                current.next.prev = current.prev

        current = next_node


    if dll.head == None:
        dll.tail = None


def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    left = dll.head
    right = dll.tail

    while left != None and right != None:
        if left.value != right.value:
            return False


        if left == right or left.next == right:
            break

        left = left.next
        right = right.prev

    return True