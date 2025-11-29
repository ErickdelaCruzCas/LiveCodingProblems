from typing import List, Optional

# Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
# Output: 0 
# Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
# Output: 3
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [0, 0]
        for student in students:
            counts[student] += 1

        remaining = len(sandwiches)
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            if remaining == 0:
                break
            counts[sandwich] -= 1
            remaining -= 1
        
        return remaining



def run_tests() -> None:
    tests: List[tuple(tuple(List[int], List[int]), int)] = [
        [([1,1,0,0], [0,1,0,1]), 0],
        [([1,1,1,0,0,1], [1,0,0,0,1,1]), 3]
        ]


    for test in tests:
        inputs, expected = test
        students, sandwiches = inputs
        result = Solution().countStudents(students, sandwiches)
        print(f"students: {students}, sandwiches: {sandwiches} => Output: {result}, Expected: {expected}")

# ----------------------------
# Ejecutar los tests
# ----------------------------
if __name__ == "__main__":
    run_tests()              
