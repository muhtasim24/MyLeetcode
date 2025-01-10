'''
we are given an integer number, and we have to convert it to a roman numeral string
roman numerals strings go from the largest to smallest just like numbers 

so it would be easy to just take each character and convert that char(int) to its associated roman numeral
but we have cases where numbers could be 2 roman numberals, like 4 is IV

for easy case no special case how we would do the math
lets say the 58
if we divide 58 by 50 , integer division, so we wouldnt get a decimal, we will get 1
which means there is 1, "50", so we would append L to our string since L = 50 in roman numerals

then we can mod our input number, 58 by 50, which would basically take away the 50 from our input
58 mod 50 = 8
so now we are at 8
we would divide our 8 by 10, 8 // 10 = 0, cant be done, so we go one step lower
8 // 5 = 1, so we know there is at least 1 5, so we can append V
string = LV so far
then we mod 8 by 5, this will give us 3
now we divide 3 by 5, this will give us 0, so we go one step lower
3 // 1 = 3, so we know we have 3, "1's so III and apend that to the string

so how can we map the roman numerals to our numbers
and go in reverse
we can create a list of tuples
[["I", 1], ["V", 5"], ["X", 10] .... ["D", 500], ["M", 1000]] we want to go through this list in reverse
so we take our input number, and divide it by each val starting from 1000,
lets say input = 500, we divide by 1000, it will give us 0, so we wouldnt do anything, we would
check the next pair in our list
if our number can divide by the number, then we can work with it
and find out how many times we need to append the roman numeral to our string to get that value
then we would update our input by modding by the value

so reverseing the list of tuples so we can append the strings from highest to smallest
if a number can be divided by a number, itll do the calculations, then go to the next
then start at that number value
if it doesnt work, itll just go to the next, works same as regular for loop

Time: O(n)
Space: O(1) since we only created a list of tuples with a definite length no matter the input

'''



class Solution:
    def intToRoman(self, num: int) -> str:
        romanInt = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
                    ["XL", 40], ["L", 50] , ["XC", 90] , ["C", 100],
                    ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]
                ]
        
        res = ""
        
        for roman, value in reversed(romanInt):
            # if the number can be divided by our value
            # that means that value exists in the num, and we have to find out
            # how many times we have to append the associated roman numeral to get that value
            if (num // value):
                count = num // value
                # this will take the string we need, multiply it the number of times we need it 
                # and append to our string 
                res += (roman * count) 
                # then we update our input num, by modding it by our assocaited value 
                num = num % value
                # next iteration will start with the next highest value in the list
                # so if this iteration we did 1000, next will check for 900
        return res
            
