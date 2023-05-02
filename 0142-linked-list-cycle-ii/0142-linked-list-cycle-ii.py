# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node_map = {}
        while(head != None):
            node_map[head] = True
            if(head.next in node_map):
                return head.next
            head = head.next
            
            
        return None