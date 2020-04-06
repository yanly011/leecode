# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if (n < 1):
            return

        signal = 1
        escape_node = head
        pre_presue_node = head
        presue_node = head

        while (escape_node.next):
            if (signal < n):
                escape_node = escape_node.next
            elif (signal == n):
                escape_node = escape_node.next
                presue_node = presue_node.next
            else:
                pre_presue_node = pre_presue_node.next
                escape_node = escape_node.next
                presue_node = presue_node.next

            signal = signal + 1
        if (signal <= n):
            head = head.next
        else:
            pre_presue_node.next = presue_node.next
        return head