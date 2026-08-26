class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        s = s.lower()
        for c in s:
            if(c.isalnum()):
                s1 += c
        def func(s1, left, right):
            if(left >= right):
                return True
            if(s1[left] != s1[right]):
                return False
            return(func(s1, left+1, right-1))

        return(func(s1, 0, len(s1) - 1))
    

    
