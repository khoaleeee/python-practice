# use sliding window with two pointers and a dictionary
# the dictionary stores the last seen index of each character
# when see duplicate, move the left pointer forward
# update the max length as I go

def lengthOfLongestSubstring(s):
    seen ={} # detect duplicate
    left = 0 #start of window
    max_len = 0 #store result

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left: #>= left to see if it's in window
            left = max(left, seen[ch] + 1)
            
        seen[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len

s = "a,b,c,a,b,c,b,b"
print(lengthOfLongestSubstring(s))