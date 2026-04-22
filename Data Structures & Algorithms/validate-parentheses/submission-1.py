class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openS = ["{", "[", "("]
        pairs = {"}": "{", "]": "[", ")": "(", }

        for char in s:
            if char in openS:
                stack.append(char)
            elif len(stack) > 0 and pairs[char] == stack[-1]:
                stack.pop()
            else:
                return False
                        

        return len(stack) == 0 

            


        print(stack)

        return True
