class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        l = min(len(word1), len(word2))
        for i in range(l):
            merge += word1[i] + word2[i]
        return merge + word1[l:] + word2[l:]