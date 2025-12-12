class Solution:
    def isPalindrome(self, s: str) -> bool:
        ini, fin = 0, len(s) - 1
        while ini < fin:

            while ini < fin and not self.alphaNum(s[ini]):
                print(s[ini])
                ini += 1
                
            while fin > ini and not self.alphaNum(s[fin]):
                print(s[fin])
                fin -= 1                

            if s[ini].lower() != s[fin].lower():
                return False
            ini += 1
            fin -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        