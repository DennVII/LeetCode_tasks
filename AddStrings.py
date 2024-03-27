DESCRIPTION = '''
Given two non-negative integers, 
num1 and num2 represented as string, 
return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly.
'''

class BigInteger():
    def __init__(self, num) -> None:
        self.num = list(map(int, [*num[::-1]]))

    def __add__(self, other):
        res = []
        next = 0
        first = self.num.copy()
        second = other.num.copy()
        while first and second:
            summa = first.pop(0) + second.pop(0) + next
            res.append(summa % 10)
            next = summa // 10
        
        while first:
            summa = first.pop(0) + next
            res.append(summa % 10)
            next = summa // 10

        while second:
            summa = second.pop(0) + next
            res.append(summa % 10)
            next = summa // 10
        
        if next:
            res.append(next)

        return BigInteger(''.join(map(str, res[::-1])))

    def get_num(self) -> str:
        return ''.join(map(str, self.num[::-1]))
 

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        bi1 = BigInteger(num1)
        bi2 = BigInteger(num2)
        return (bi1 + bi2).get_num()
    

s = Solution()
print(s.addStrings('1', '9'))
