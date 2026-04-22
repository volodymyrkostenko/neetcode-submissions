class Solution:
    def isValid(self, s: str) -> bool:
        
        s_open = ["(", "{", "["]

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for char in s:
            if char in s_open:
                stack.append(char)
                continue
            
            if len(stack) == 0:
                return False
            
            last_element = stack.pop()

            if pairs[char] != last_element:
                return False
          


        return len(stack) == 0