# 给定一个单链表中的一个等待被删除的节点(非表头或表尾)。请在在O(1)时间复杂度删除该链表节点。（脑洞开大点）
# 给定 1->2->3->4，和节点 3，删除 3 之后，链表应该变为 1->2->4

class Node:
    def __init__(self,val,_next=None):
        self.val= val
        self.next=next
def deleteNode(node):
    return 0