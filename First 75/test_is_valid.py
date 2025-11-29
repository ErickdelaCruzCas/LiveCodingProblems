# pylint: disable=missing-module-docstring, missing-class-docstring

class Solution:
    def isValid(self, s: str) -> bool:
        specialcharsMap = {")":"(", "]":"[","}":"{"}
        acum = []
        for c in s:
            if c in specialcharsMap.values():
                acum.append(c)
            else:  
                if acum and acum[-1] == specialcharsMap[c]:
                    acum.pop()
                else:
                    return False
        return True and len(acum) == 0
        

# ------------------------------------------------------------
# Casos de prueba
# ------------------------------------------------------------

tests = [
    ("", True),
    ("()", True),
    ("[]", True),
    ("{}", True),
    ("()[]{}", True),
    ("({[]})", True),
    ("[({})]", True),
    ("((()))", True),
    ("{[()()]}", True),

    # incorrectos simples
    ("(]", False),
    ("([)]", False),
    ("((", False),
    (")(", False),
    ("]]", False),
    ("[", False),
    ("]", False),

    # intermedios
    ("(()[])", True),
    ("([{}{}])", True),
    ("([{}{}])]", False),
    ("{([])}[", False),
    ("(([]){{}})", True),
    ("{[()]]", False),

    # largos
    ("()" * 100, True),
    ("[]" * 200, True),
    ("(" * 500, False),
    (")" * 500, False),

    # maliciosos
    ("([[[[{{{{((()))}}}}]]]])", True),
    ("([[[[{{{{((()))}}}}]]]])}", False),
    ("(((((((((())))))))))", True),
    ("(((((((((())))))))))(", False),
    ("{}{}{}{}[][][][]()()()", True),
    ("{[([([([([([)])])])])]", False),

    # inicios incorrectos
    (")([])", False),
    ("]()()", False),
    ("}{}}", False),
]

# ------------------------------------------------------------
# Ejecutor
# ------------------------------------------------------------
solution = Solution()

for inp, expected in tests:
    try:
        result = solution.isValid(inp)
    except Exception as e:
        print(f"❌ ERROR ejecutando s={inp!r}: {e}")
        continue

    if result == expected:
        print(f"✅ OK  s={inp!r} → {result}")
    else:
        print(f"❌ FAIL s={inp!r} → {result} (expected {expected})")
