from collections import Counter
def highfreq(n):
    freq=Counter(n)
    max_freq=max(freq.values())
    result=[n for n in freq if freq[n]==max_freq]
    return min(result)
n=[2,2,2,3,1]
print(highfreq(n))