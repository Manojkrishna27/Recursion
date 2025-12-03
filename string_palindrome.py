# checking a string is a palindrome we have some methods

# method 1 slicing

n="121"
s=n[::-1]
if n==s:
    print("Palindrome")
else:
    print("not")

#  method 2two pointer
n="madam"
i=0
j=len(n)-1
ispalindrome=True
while i<j:
    if n[i]!=n[j]:
        ispalindrome=False
        break
    i=i+1
    j=j-1
if (ispalindrome):
    print("palindrome")
else:
    print("not a palindrome")
