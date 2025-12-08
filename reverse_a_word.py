class Solution:
    def rev(self,s):
        word=s.split()
        word.reverse()
         
        return " ".join(word)
output=Solution()
print(output.rev("sky is blue"))