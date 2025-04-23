class Solution:
    def addDigits(self, num: int) -> int:
        while(num > 9):
            temp = 0
            while num:
                temp = temp + num%10
                num//=10
            num = temp
        return num

newitem = Solution()    

for i in range(1,250):
    print(i,newitem.addDigits(i))


# # the above methode works fine but it have o(n time complexity since we have loop)


# but when we print the values it shows the remainder for the given number if its divided by 9.therefor we can use the modulo operator to get the sum of the digits.but since the module of 9 by it self will be zoro we now the multiple of 9,and the sum of the multile of nine is 9 itself.

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

newitem = Solution()    

for i in range(1,250):
    print(i,newitem.addDigits(i))
        