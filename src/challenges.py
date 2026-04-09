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

<<<<<<< HEAD
    Examples:
        >>> sll_to_list(build_sll_from_list([]))
        []
        >>> sll_to_list(build_sll_from_list([4, 7, 9]))
        [4, 7, 9]
    """
    sll = SinglyLinkedList()

    if len(values) == 0:
        return sll

    # create first node
    sll.head = SLLNode(values[0])
    current = sll.head

    # add remaining nodes
=======
    if len(values) == 0:
        return sll

    sll.head = SLLNode(values[0])
    current = sll.head

>>>>>>> bb4937aeab0357255b676a8256e7347290d120fd
    for i in range(1, len(values)):
        new_node = SLLNode(values[i])
        current.next = new_node
        current = new_node

    return sll
<<<<<<< HEAD

    raise NotImplementedError


def sll_to_list(sll: SinglyLinkedList) -> list[int]:
    """Return all values from a singly linked list as a Python list."""
=======


def sll_to_list(sll: SinglyLinkedList) -> list[int]:
>>>>>>> bb4937aeab0357255b676a8256e7347290d120fd
    result = []
    current = sll.head

    while current != None:
        result.append(current.value)
        current = current.next

    return result
<<<<<<< HEAD
    raise NotImplementedError
=======

>>>>>>> bb4937aeab0357255b676a8256e7347290d120fd


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

<<<<<<< HEAD
    Return None if no value repeats.
    """
    seen = []  
    current = sll.head

    while current != None:
        if current.value in seen:
            return current.value
        else:
            seen.append(current.value)

        current = current.next

    return None
    raise NotImplementedError
=======
>>>>>>> bb4937aeab0357255b676a8256e7347290d120fd


def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    current = dll.head

<<<<<<< HEAD
    Update dll.head and dll.tail correctly.
    Return None.
    """
    current = dll.head

    while current != None:
        next_node = current.next  

        if current.value == target:
=======
    while current != None:
        next_node = current.next
        if current.value == target:

>>>>>>> bb4937aeab0357255b676a8256e7347290d120fd
            if current.prev == None:
                dll.head = current.next
                if dll.head != None:
                    dll.head.prev = None

<<<<<<< HEAD
=======

>>>>>>> bb4937aeab0357255b676a8256e7347290d120fd
            elif current.next == None:
                dll.tail = current.prev
                if dll.tail != None:
                    dll.tail.next = None

<<<<<<< HEAD
=======

>>>>>>> bb4937aeab0357255b676a8256e7347290d120fd
            else:
                current.prev.next = current.next
                current.next.prev = current.prev

        current = next_node

<<<<<<< HEAD
    if dll.head == None:
        dll.tail = None
    raise NotImplementedError


def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    """Stretch: return True if the DLL reads the same forward and backward."""
=======

    if dll.head == None:
        dll.tail = None


def is_train_palindrome(dll: DoublyLinkedList) -> bool:
>>>>>>> bb4937aeab0357255b676a8256e7347290d120fd
    left = dll.head
    right = dll.tail

    while left != None and right != None:
        if left.value != right.value:
            return False

<<<<<<< HEAD
        # stop when pointers meet or cross
=======

>>>>>>> bb4937aeab0357255b676a8256e7347290d120fd
        if left == right or left.next == right:
            break

        left = left.next
        right = right.prev

<<<<<<< HEAD
    return True
    raise NotImplementedError
=======
    return True
>>>>>>> bb4937aeab0357255b676a8256e7347290d120fd
