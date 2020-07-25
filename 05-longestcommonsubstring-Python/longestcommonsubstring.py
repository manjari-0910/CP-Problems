# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    i=0
    a=s1
    li=[]
    while i<=len(a):
        j=0
        while(i+j<=len(a)):
            if len(a[i:i+j])>0:
                li.append(a[i:i+j])
            j+=1
        i+=1
    l2 = sorted(li, key=len)
    for i in l2[::-1]:
        if i in s2:
            return i
    return ''
    pass
