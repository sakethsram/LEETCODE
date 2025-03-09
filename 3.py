from typing import List
def kidsWithCandies( candies: List[int], extraCandies: int) -> List[bool]:
    
    big = max(candies)
    res = [False] * len(candies)
    for i in range (len(candies)):
        if ((candies[i] + extraCandies) >= big): res[i] = True
    print(res) 
    return  res

candies =[2,3,5,1,3] 
extraCandies =3 
kidsWithCandies(candies , extraCandies)