'''
Author: mxh970120
Date: 2020.12.18
'''

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        if not head.next:
            return head

        # current-->cur 当前项
        # previous-->prev 前一项
        prev, cur = head, head.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head





