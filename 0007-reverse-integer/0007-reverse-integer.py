class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if(x < 0):
            flag = True
            x *= -1
        rev = 0
        while x > 0:
            dig = x % 10
            rev = rev * 10 + dig
            x = x // 10
        
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
            
        if(not flag):
            return rev
        else:
            return -rev
