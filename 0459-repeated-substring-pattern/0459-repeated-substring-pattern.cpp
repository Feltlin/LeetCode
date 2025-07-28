class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        for(int i = 1; i <= s.length() / 2; ++i){
            if(s.length() % i == 0){
                std::string k = s.substr(0, i);
                std::string m = "";
                while(m.length() < s.length()){
                    m += k;
                }
                if(m == s){
                    return true;
                }
            }
        }
        return false;
    }
};