class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode(0)
        current_node = head

        pointer_list = []

        for i in range(len(lists)):
            pointer_list.append(lists[i])

        end_counter = 0

        while end_counter < len(lists):

            loop_min = 100
            loop_index = None

            for k in range(len(pointer_list)):

                if pointer_list[k] == None:
                    continue

                if pointer_list[k].val <= loop_min:
                    loop_min = pointer_list[k].val
                    loop_index = k

            if loop_index == None:
                break

            value = pointer_list[loop_index].val
            new_node = ListNode(value)
            current_node.next = new_node
            current_node = new_node

            pointer_list[loop_index] = pointer_list[loop_index].next

            if pointer_list[loop_index] == None:
                end_counter += 1

        return head.next