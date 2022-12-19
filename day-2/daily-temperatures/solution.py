from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = len(temperatures)
        answer = [0 for i in range(days)]

        if len(set(temperatures)) == 1:
            return answer

        prev_days = [0]

        for i in range(1, days):
            temp = temperatures[i]
            prev = prev_days[-1]

            while len(prev_days) and temp > temperatures[prev_days[-1]]:
                prev = prev_days.pop()
                answer[prev] = i - prev

            prev_days.append(i)

        return answer