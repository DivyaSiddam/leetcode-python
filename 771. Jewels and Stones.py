# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for i in jewels:
           for j in stones:
                print(i,j)
                if i==j:
                    ans=ans + 1
        return(ans)
