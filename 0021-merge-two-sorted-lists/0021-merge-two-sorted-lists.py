# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(0)
        current_output = head

        current_l1 = list1
        current_l2 = list2

        while current_l1 != None and current_l2 != None:

            if current_l1.val <= current_l2.val:
                current_output.next = current_l1
                current_output = current_output.next
                current_l1 = current_l1.next

            else:
                current_output.next = current_l2
                current_output = current_output.next
                current_l2 = current_l2.next

        while current_l1 != None:
                current_output.next = current_l1
                current_output = current_output.next
                current_l1 = current_l1.next
        
        while current_l2 != None:
                current_output.next = current_l2
                current_output = current_output.next
                current_l2 = current_l2.next

        head = head.next
        
        return head