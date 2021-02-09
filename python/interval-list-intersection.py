class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        
        while i < len(firstList) and j < len(secondList):
            if (
                secondList[j][0] <= firstList[i][1] <= secondList[j][1] or
                firstList[i][0] <= secondList[j][1] <= firstList[i][1]
            ):
                res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return res