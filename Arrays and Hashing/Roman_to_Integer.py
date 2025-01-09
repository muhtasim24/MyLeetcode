'''
we are given a string of roman numerals
we have to convert the string to the actual value as a number, an int
so we have symbols 
I : 9
V : 5
X : 10
L : 50
C : 100
D : 500
M : 1000

so we can create a hashmap to map the string to the int value
for every character in the string we add to our total based on its int val

XII 
X = 10
I = 1
I = 1
10 + 1 + 1 = 12

but what about cases like IV, which is 4
we cant do I + V, because then that would give us 1 + 5 = 6

so for IV we actually subtract
5 - 1 = 4

IV = 5 - 1 = 4
IX = 10 - 1 = 9

XL = 50 - 10 = 40
XC = 100 - 10 = 90

CD = 500 - 100 = 400
CM = 1000 - 100 = 900

so we are garuanteed valid string
that means larger values come first before the smaller value
UNLESS its one of the 6 instances
thats the only time when the val of the first character is smaller than the next

so we can just iterate through the string
use our map to associate the character with the int val
if map[i] is smaller than map[i + 1]

edge case when checking for i + 1, we should also make sure i + 1 is smaller than the length of the array
so we are not going out of bounds

then our current val, we can just treat as negative, and subtract it from our total

but for any other case, we treat as normal, and just add the val to our total



Time: O(n)
Space: O(1)
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {
            "I": 1 , "V" : 5, "X" : 10, "L" : 50,
            "C": 100, "D" : 500, "M": 1000
        }

        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and romanMap[s[i]] < romanMap[s[i + 1]]:
                total -= romanMap[s[i]]
            else:
                total += romanMap[s[i]]
        
        return total
                
