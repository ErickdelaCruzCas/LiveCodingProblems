from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode, nextNode = head, head
        previousNode = None        
        while currentNode:
            nextNode = currentNode.next    
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode            
        return previousNode
     

def list_to_linkedlist(values: List[int]) -> Optional[ListNode]:
    """Convierte una lista de Python en una lista enlazada (ListNode)."""
    if not values:
        return None
    head: ListNode = ListNode(values[0])
    current: ListNode = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


def linkedlist_to_list(node: Optional[ListNode]) -> List[int]:
    """Convierte una lista enlazada (ListNode) en una lista de Python."""
    result: List[int] = []
    while node:
        result.append(node.val)
        node = node.next
    return result
    

# ----------------------------
# Casos de prueba estilo LeetCode
# ----------------------------
def run_tests() -> None:
    test_cases: List[tuple[List[int], List[int]]] = [
        ([1,2,3,4,5], [5,4,3,2,1]),
        ([1,2], [2,1]),
        ([1], [1]),
        ([], []),
        ([1,1,1,2,2], [2,2,1,1,1])
    ]

    for i, (input_list, expected_output) in enumerate(test_cases, 1):
        head: Optional[ListNode] = list_to_linkedlist(input_list)
        result: Optional[ListNode] = Solution().reverseList(head)
        result_list: List[int] = linkedlist_to_list(result)
        print(f"Test {i}: Input={input_list}")
        print(f"Output:   {result_list}")
        print(f"Expected: {expected_output}")
        print("✅" if result_list == expected_output else "❌", "\n")

# ----------------------------
# Ejecutar los tests
# ----------------------------
if __name__ == "__main__":
    run_tests()