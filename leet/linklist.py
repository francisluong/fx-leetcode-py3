from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def values(self):
        result = []
        this = self
        while this.next:
            result.append(this.val)
            this = this.next
        # finally
        result.append(this.val)
        return result


def into_list_nodes(node_values: List[any]) -> ListNode:
    prev = None
    for val in reversed(node_values):
        node = ListNode(val=val, next=prev)
        prev = node
    return node
