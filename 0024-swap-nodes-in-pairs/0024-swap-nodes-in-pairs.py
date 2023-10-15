class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        list_of_nodes = []

        current_node = head

        while current_node != None:
            list_of_nodes.append(current_node)
            current_node = current_node.next

        if len(list_of_nodes) <= 1:
            return head

        if len(list_of_nodes) % 2 == 0:
            zap = None
            starting_point = 2

        else:
            zap = list_of_nodes[-1]
            starting_point = 3

        for i in range(len(list_of_nodes) - starting_point, -1, -2):

            list_of_nodes[i].next = zap
            list_of_nodes[i+1].next = list_of_nodes[i]
            zap = list_of_nodes[i+1]

        return list_of_nodes[1]