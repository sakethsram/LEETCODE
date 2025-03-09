def reverseVowels(s):
    def isvowel(a): return a.lower() in "aeiou"

    s = list(s)
    n = len(s)
    i, j = 0, n - 1

    while i < j:
        if not isvowel(s[i]):
            i += 1
        elif not isvowel(s[j]):
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    return ''.join(s)  # Convert list back to string
print(reverseVowels("hello"))  # Output: "holle"
print(reverseVowels("leetcode"))  # Output: "leotcede"
