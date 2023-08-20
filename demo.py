'''Given a string s, remove all its adjacent duplicate characters recursively.
Input:

Output: "gksforgk"
Explanation:
g(ee)ksforg(ee)k -> gksforgk'''


def remove_duplicates():
    

    if len(s) <=1:
        return 1
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i-1]:
            s = s[:i] + s[i + 2:]
            i = max(0, i-1) 
        else:
            i += 1
    return remove_duplicates(s)
s = "geeksforgeek"
print(remove_duplicates(s))


