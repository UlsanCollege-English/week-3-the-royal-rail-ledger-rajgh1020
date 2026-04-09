# Week 3: The Royal Rail Ledger

## Summary
This assignment focuses on linked-list operations in a railway story setting. I implemented functions for building and reading a singly linked list, finding the first repeated value, removing banned cargo from a doubly linked list, and checking whether a train is a palindrome. The assignment uses both singly linked lists and doubly linked lists. The hardest part was updating pointers correctly in the doubly linked list when removing nodes.

---

## Approach

### `build_sll_from_list(values)`
- I started with creating an empty singly linked list  
- I built the list by creating nodes one by one and linking them using `next`  
- I made sure the values stayed in the correct order by adding nodes from left to right  

### `sll_to_list(sll)`
- I started at the head of the linked list  
- I traversed the list by moving to the next node each time  
- I collected values in a Python list by appending each node’s value  

### `find_first_repeat_sll(sll)`
- I tracked values I had already seen by using a simple Python list  
- When I found a repeated value, I returned it immediately  
- If I reached the end with no repeat, I returned `None`  

### `remove_all_from_dll(dll, target)`
- I traversed the list using a `current` pointer  
- When I found the target value, I updated `prev` and `next` pointers to remove the node  
- I checked special cases such as removing the head, tail, and when the list becomes empty  

### `is_train_palindrome(dll)`
- I compared values from the head and tail moving towards the center  
- I stopped when the pointers met or crossed each other  
- I returned `True` or `False` based on whether all values matched  

---

## Complexity

### `build_sll_from_list(values)`
- **Time complexity:** O(n)  
- **Space complexity:** O(n)  
- **Why:** I loop through the list once and create one node for each value  

### `sll_to_list(sll)`
- **Time complexity:** O(n)  
- **Space complexity:** O(n)  
- **Why:** I traverse the list once and store values in a new list  

### `find_first_repeat_sll(sll)`
- **Time complexity:** O(n²)  
- **Space complexity:** O(n)  
- **Why:** I check each value in a list using `in`, which takes extra time  

### `remove_all_from_dll(dll, target)`
- **Time complexity:** O(n)  
- **Space complexity:** O(1)  
- **Why:** I go through the list once and only change pointers  

### `is_train_palindrome(dll)` *(stretch)*
- **Time complexity:** O(n)  
- **Space complexity:** O(1)  
- **Why:** I compare from both ends without using extra space  

---

## Edge-Case Checklist

- [x] empty SLL  
- [x] empty DLL  
- [x] single-node SLL  
- [x] single-node DLL  
- [x] no repeated values in SLL  
- [x] repeated value appears later in SLL  
- [x] repeated value includes the head value  
- [x] removing from DLL when target is at head  
- [x] removing from DLL when target is at tail  
- [x] removing consecutive target values in DLL  
- [x] removing all nodes from DLL  
- [x] palindrome with odd length  
- [x] palindrome with even length  
- [x] non-palindrome DLL  

---

## Assistance & Sources

### AI use
- I used AI: Yes  
- It helped me understand how to handle pointer updates and debug my logic  

### Other sources
- Class notes: Yes  
- Slides: Yes  
- Book: No  
- Websites: No  
- Other: None  

---

## Debugging Notes

- I first got stuck on removing nodes in the doubly linked list  
- The failing test that helped me most was when removing all nodes  
- I fixed the issue by carefully updating both `prev` and `next` pointers  
- One mistake I will avoid next time is forgetting to update the `tail`  

---

## Final Reflection

This assignment helped me understand how linked lists work internally. Doubly linked lists were harder because of pointer updates. The most surprising edge case was when the entire list gets deleted. Before the next assignment, I will review pointer handling and traversal logic.