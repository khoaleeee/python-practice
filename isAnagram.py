# count characters frequency in both strings using hash maps
# if both maps are equal, the strings are anagrams


def isAnagrams(s,t):
    if len(s) != len(t):
        return False
    
    count ={}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] == 0:
            del count[ch]

    return True

s = "abc"
t = "bac"
print(isAnagrams(s,t))
    