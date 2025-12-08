class Solution:
    def rev(self,s):
        word=s.split()
        reverse=(w[::-1] for w in word)
        return " ".join(reverse)
output=Solution()
print(output.rev("hi i am manoj"))