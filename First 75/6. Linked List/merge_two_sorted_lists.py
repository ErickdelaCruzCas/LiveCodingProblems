from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next



def list_to_linkedlist(values: List[int]) -> Optional[ListNode]:
    node = ListNode(values[0])
    head = node
    for value in values[1:]:
        node.next = ListNode(value)
        node = node.next
    return head

def linkedlist_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
    
# ----------------------------
# Casos de prueba estilo LeetCode
# ----------------------------
def run_tests() -> None:
    test_cases: List[tuple[List[int], List[int], List[int]]] = [
        ([1,2,3,4,5], [2,3,5,6,7], [1,2,2,3,3,4,5,6,7]),
        ([1,2], [2,1], [1,1,2,2]),
        ([1], [1], [1,1]),
        ([], [], []),
        ([1,1,1,2,2], [2,2,2,2,3], [1,1,1,2,2,2,2,2,2,3])
    ]
    
    for i, (input_list1, input_list2, expectedList) in enumerate(test_cases, 1):
        head1: Optional[ListNode] = list_to_linkedlist(input_list1) 
        head2: Optional[ListNode] = list_to_linkedlist(input_list2) 
        result:Optional[ListNode] = Solution().mergeTwoLists(head1, head2)
        result_list: List[int] = linkedlist_to_list(result)
        print(f"Test {i}: Input={input_list1} and {input_list2}")
        print(f"Output:   {result_list}")
        print(f"Expected: {expectedList}")
        print("✅" if result_list == expectedList else "❌", "\n")
     
# ----------------------------
# Ejecutar los tests
# ----------------------------
if __name__ == "__main__":
    run_tests()       
    