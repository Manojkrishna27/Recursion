# reverse string using slicing
name="manoj"
rev=name[::-1]
print(rev)
# using logic

name="manoj"
rev=""
for ch in name:
    rev=ch+rev
print(rev)
