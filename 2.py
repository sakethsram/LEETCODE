from math import gcd
def gcdOfStrings(word1,word2) :
    result=''  
    if word1+word2==word2+word1 :
        t = gcd (len(word1),len(word1)) 
        return word1[0:t]
    return ""