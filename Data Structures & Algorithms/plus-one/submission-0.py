class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ten = 10**(len(digits)-1)
        digit = digits[0] * ten
        for i in digits[1:]:
            ten /= 10
            digit += i * ten
        digit = int(digit+1)
        digit = str(digit)
        return list(map(int, list(digit)))
            