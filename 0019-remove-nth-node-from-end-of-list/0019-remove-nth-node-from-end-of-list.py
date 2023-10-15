class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def check_list_length(head):

            current = head
            counter = 0
            while current is not None:
                current = current.next
                counter += 1

            return counter
        

        list_length = check_list_length(head)
        node_to_delete = list_length - (n-1)
        last_node = False

        if list_length <= 1:
            return None

        elif list_length == node_to_delete:
            last_node = True

        if node_to_delete == 1:
            return head.next

        current = head
        counter = 1
        while counter < node_to_delete-1:
            current = current.next
            counter += 1

        if last_node == True:
            current.next = None
        else:
            current.next = current.next.next

        return head