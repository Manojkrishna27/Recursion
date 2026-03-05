NAME="Goodmorning"
Decode="o"
freq={}
for ch in NAME:
    freq[ch]=freq.get(ch,0)+1
for ch in freq:
    if ch ==Decode:
        print(freq[ch])