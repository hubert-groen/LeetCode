class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        list_of_nodes = []
        current_node = head

        while current_node != None:
            list_of_nodes.append(current_node)
            current_node = current_node.next

        unchanged_end = len(list_of_nodes) % k

        if unchanged_end == 0:
            zap = None
        else:
            zap = list_of_nodes[- unchanged_end]

        for i in range(len(list_of_nodes)-1-unchanged_end, -1, -k):

            for j in range(k):
                list_of_nodes[i-j].next = list_of_nodes[i-j-1]

            list_of_nodes[i-k+1].next = zap
            zap = list_of_nodes[i]

        return list_of_nodes[k-1]