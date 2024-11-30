class Solution {
public:
    int mySqrt(int x) {
        long long root = 0;
        long long i = 0;
        while (i <= x){
            i = root * root;
            if (i > x){
                break;
            }
            ++root;
        }
        if (i > x){
            return root - 1;
        }
        else{
            return root;
        }
    }
};