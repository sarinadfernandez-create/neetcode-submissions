class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if stack and (ch == ")" or ch == "]" or ch == "}"):
                if stack[-1]=="(" and ch==")":
                    stack.pop()
                elif stack[-1]=="[" and ch=="]":
                    stack.pop()
                elif stack[-1]=="{" and ch=="}":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        if stack == []:
            return True 
        else:
            return False

            