def reverseWords(s: str) -> str:
 s=s.split()
 s.reverse()
 
 print (s)
 s = ' '.join(s)  # Join list elements with a space
 print (s)
 return s


s="a good   example"
 
reverseWords(s)