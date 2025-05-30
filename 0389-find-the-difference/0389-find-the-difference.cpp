class Solution {
public:
    char findTheDifference(string s, string t) {
        std::unordered_map<char, int> count;
        for(char i : t){
            ++count[i];
        }
        for(char i : s){
            --count[i];
            if(count[i] == 0){
                count.erase(i);
            }
        }
        return count.begin()->first;
    }
};