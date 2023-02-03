# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        h = []
        for idx, l in enumerate(lists):
            if l:
                h.append((l.val, idx))
        heapify(h)
        head = curr = ListNode(None)
        while h:
            val, idx = heappop(h)
            curr.next = lists[idx]
            curr = curr.next
            lists[idx] = lists[idx].next
            node = lists[idx]
            if node:
                heappush(h, (node.val, idx))
        return head.next