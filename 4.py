from typing import List

def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed.count(0) < 2 * n:  
            return False

        if len(flowerbed) > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n =n - 1

        if len(flowerbed) > 1 and flowerbed[-1] == 0 and flowerbed[-2] == 0: 
            flowerbed[-1] = 1
            n -= 1
            
        for i in range (1,len(flowerbed)-1):
            if(flowerbed[i]==0 and flowerbed[i]==0 and flowerbed[i+1]==0  ):
                flowerbed[i]==1
                n=n-1
        
        if n<1:return True
        return False
            
        