class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        daily = []
        for i in range(len(temperatures)-1):
            for j in range (i+1, len(temperatures)):
                    if temperatures[j] > temperatures[i]:
                        daily.append(j-i)
                        break
                    elif j == len(temperatures)-1 :
                        daily.append(0) 
        daily.append(0)
                
        return daily

            
