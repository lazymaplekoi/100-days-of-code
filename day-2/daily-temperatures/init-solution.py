from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = len(temperatures)
        answer = [1 for i in range(days)]
        answer[-1] = 0

        sorted_temp = sorted(temperatures)

        # base case: sorted temperatures
        if sorted_temp == temperatures:
            return answer

        for i in range(days - 1):
            temp = temperatures[i]
            if temp == sorted_temp[-1]: 
                answer[i] = 0
                continue
            if (temp < temperatures[i+1]): 
                answer[i] = 1
                continue

            future = [t - temp for t in temperatures[i+1:]]
            next_warm_day = next((future.index(x) for x in future if x > 0), -1)
            answer[i] = next_warm_day + 1

        return answer