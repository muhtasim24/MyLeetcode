class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        original = []
        tList = []
        for i in s:
            original.append(i)
        
        for i in t:
            tList.append(i)
            
        if len(original) != len(tList):
            return False
            
        for i in original:
            for j in tList:
                if i not in tList:
                    return False
                if j not in original:
                    return False
        return True
