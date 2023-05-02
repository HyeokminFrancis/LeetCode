# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return None
        
        node_list = []
        while(head != None):
            node_list.append(head)
            head = head.next
        
        
        return node_list[int(len(node_list)/2)]
        