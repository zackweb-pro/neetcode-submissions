class Solution:
    def isHappy(self, n: int) -> bool:
        arr = []
        c = n
        while c not in arr:
            arr.append(c)
            a = (c - c%1000)//1000
            b = (c%1000 - c%100)//100
            k = (c%100 - c%10)//10
            d = c%10
            c = a**2+b**2+k**2+d**2
            print(a,b,c,d, c)
            if c == 1:
                return True
        else:
            return False