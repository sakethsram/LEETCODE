def mergeAlternately(word1: str, word2: str):
    if len(word1) < len(word2):
        s,big = word1, word2
    else:
        big, s = word1, word2

    temp = big[len(s):] 
    big=big[0:len(s)]
    res=''
    for i in range(len(big)):    
        res=res + word1[i]
        res=res + word2[i]
    res=res+temp
    print(res)

    return res

word1 = "abc"
word2 = "pqr"
mergeAlternately(word1,word2)        