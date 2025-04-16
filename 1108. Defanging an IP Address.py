#https://leetcode.com/problems/defanging-an-ip-address/
class Solution:
    def defangIPaddr(self, address: str) -> str:
      ans=""
      for i in address:
         if i ==".":
           ans = ans + "[.]"
         else:
           ans = ans + i
      return ans
