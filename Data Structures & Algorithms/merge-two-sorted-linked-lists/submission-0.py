# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_hh = []
        list2_hh = []
        while list1:
            list1_hh.append(list1.val)
            list1 = list1.next
        while list2:
            list2_hh.append(list2.val)
            list2 = list2.next
        list_hh = sorted(list(list1_hh + list2_hh))
        dummy = ListNode(-1)
        curr = dummy
        for v in list_hh:
            curr.next  = ListNode(v)
            curr = curr.next
        return dummy.next