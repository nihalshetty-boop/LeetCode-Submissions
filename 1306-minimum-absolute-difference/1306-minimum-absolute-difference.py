class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        minc = float('inf')

        for i in range(1, len(arr)):
            if(arr[i]-arr[i-1]<minc):
                minc = arr[i]-arr[i-1]

        for i in range(1, len(arr)):
            if(arr[i]-arr[i-1]==minc):
                ans.append([arr[i-1], arr[i]])

        return ans