class Solution:
    def longestNonRepeatingSubstring(self, s):
        n=len(s)
        left=0
        sett=set()
        maxlen=0
        for right in range(n):
            while  s[right] in sett:
                sett.remove(s[left])
                left+=1
            sett.add(s[right])
            maxlen=max(maxlen,right-left+1)
        return maxlen
a=Solution()
s="abcddabac"
print(a.longestNonRepeatingSubstring(s))
           

                
        