# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        src, dest = (list1, list2)

        if list1.val < list2.val:
            src = list2
            dest = list1

        head = dest

        while src:
            while dest.next and dest.next.val <= src.val:
                dest = dest.next
            
            dest.next = ListNode(src.val, dest.next)
            src = src.next
        
        return head