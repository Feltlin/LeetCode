class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);
        string r = "";
        for (int i = 0; i < s.length(); ++i){
            r += s.at(s.length() -1 - i);
        }
        return s == r;
    }
};