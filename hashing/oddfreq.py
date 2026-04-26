def oddfreq(word):
    freq={}
    for ch in word:
        freq[ch]=freq.get(ch,0)+1
    for key in freq:
        if freq[key]%2!=0:
            print(key,freq[key])
word="aabbccc"
print(oddfreq(word))