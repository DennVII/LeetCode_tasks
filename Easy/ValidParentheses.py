#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
    #Open brackets must be closed by the same type of brackets.
    #Open brackets must be closed in the correct order.
    #Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        index = 0
        while index < len(s):
            if s[index] in '{[(':
                stack.append(s[index])
            elif s[index] in '}])':
                if len(stack) == 0:
                    return False
                if (stack[-1] == '[' and s[index] == ']') or \
                    (stack[-1] == '{' and s[index] == '}') or \
                    (stack[-1] == '(' and s[index] == ')'):
                    stack.pop()
                else:
                    return False
            index += 1
        if(len(stack) > 0):
            return False
        return True

