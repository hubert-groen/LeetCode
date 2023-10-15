from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values: List[int]) -> Optional[ListNode]:

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = new_node

    return head

    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(0)
        current_NODE = head
        pass_further = 0
        
        while l1 is not None or l2 is not None or pass_further != 0:

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            digit_sum = l1_val + l2_val + pass_further

            print(f"Digit sum = {digit_sum}")

            if digit_sum > 9:
                pass_further = digit_sum // 10
                digit_sum = digit_sum % 10
            else:
                pass_further = 0

            print(f"pass_further = {pass_further}")
            print(f"digit_sum = {digit_sum}")

            new_NODE = ListNode(digit_sum)
            current_NODE.next = new_NODE
            current_NODE = new_NODE

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next


    
head_1 = create_linked_list([2,4,3])
head_2 = create_linked_list([5,6,4])

n = Solution()
new_head = n.addTwoNumbers(head_1,head_2)

print("---------------")

current = new_head
while current is not None:
    print(current.val)
    current = current.next