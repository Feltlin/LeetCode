class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::string merge = "";
        int l = std::min(word1.length(), word2.length());
        for(int i = 0; i < l; ++i){
            merge = merge + word1[i] + word2[i];
        }
        return merge + word1.substr(l) + word2.substr(l);
    }
};