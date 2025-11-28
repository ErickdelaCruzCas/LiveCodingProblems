class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]      

    def getMin(self) -> int:
        return self.min_stack[-1]      
    
    
    
    
# ------------------------------------------------------------
# Ejecutor
# ------------------------------------------------------------ 

# Asume que tu clase se llama MinStack
# Ejemplo de batería de pruebas estilo LeetCode

def run_tests():
    tests = [
        {
            "name": "Básico",
            "ops": ["MinStack", "push", "push", "getMin", "top", "pop", "getMin", "top"],
            "args": [[], [2], [1], [], [], [], [], []],
            "expected": [None, None, None, 1, 1, None, 2, 2],
        },
        {
            "name": "Mínimos duplicados",
            "ops": ["MinStack", "push", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin", "top"],
            "args": [[], [3], [5], [2], [2], [], [], [], [], [], []],
            "expected": [None, None, None, None, None, 2, None, 2, None, 3, 5],
        },
        {
            "name": "Creciente",
            "ops": ["MinStack", "push", "push", "push", "getMin", "top", "pop", "getMin", "pop", "getMin"],
            "args": [[], [1], [2], [3], [], [], [], [], [], []],
            "expected": [None, None, None, None, 1, 3, None, 1, None, 1],
        },
        {
            "name": "Decreciente",
            "ops": ["MinStack", "push", "push", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
            "args": [[], [5], [4], [3], [2], [1], [], [], [], [], []],
            "expected": [None, None, None, None, None, None, 1, None, 2, None, 3],
        },
        {
            "name": "Negativos y cero",
            "ops": ["MinStack", "push", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin", "pop", "getMin"],
            "args": [[], [0], [-1], [-1], [2], [], [], [], [], [], [], []],
            "expected": [None, None, None, None, None, -1, None, -1, None, -1, None, 0],
        },
    ]

    for test in tests:
        print(f"\nRunning test: {test['name']}")
        stack = None
        results = []
        for op, arg in zip(test["ops"], test["args"]):
            if op == "MinStack":
                stack = MinStack()
                results.append(None)
            elif op == "push":
                results.append(stack.push(*arg))
            elif op == "pop":
                results.append(stack.pop())
            elif op == "top":
                results.append(stack.top())
            elif op == "getMin":
                results.append(stack.getMin())
        print("Results:  ", results)
        print("Expected: ", test["expected"])
        print("✅" if results == test["expected"] else "❌")

# Llama a la función si ejecutas este script directamente
if __name__ == "__main__":
    run_tests()   