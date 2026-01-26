class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = arr[1] - arr[0]
        pair = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] < diff:
                diff = arr[i + 1] - arr[i]
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == diff:
                pair.append([arr[i], arr[i + 1]])
        return pair