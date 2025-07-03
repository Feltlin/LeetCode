class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a) + int(b)
        return bin(int(a, 2) + int(b, 2))[2:]