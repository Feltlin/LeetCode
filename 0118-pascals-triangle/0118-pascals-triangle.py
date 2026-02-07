class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        else:
            l = [[1], [1, 1]]
            while len(l) < numRows:
                k = [1, 1]
                for i in range(len(l) - 1):
                    k.insert(-1, l[-1][i] + l[-1][i + 1])
                l.append(k)
            return l