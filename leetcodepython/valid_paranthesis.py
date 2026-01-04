class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            # opening bracket
            if ch in mapping.values():
                stack.append(ch)
            else:
                # closing bracket but stack empty
                if not stack:
                    return False
                
                top = stack.pop()
                if mapping[ch] != top:
                    return False

        return len(stack) == 0
