# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return None

        node_list = []
        curr = head
        while(curr != None):
            node_list.append(curr)
            curr = curr.next
        
        node = node_list[-1]
        for idx in range(len(node_list)-1,-1, -1):
            if(idx == 0):
                node_list[idx].next = None
            else:
                node_list[idx].next = node_list[idx-1]

        return node

