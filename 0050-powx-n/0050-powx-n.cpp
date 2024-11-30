class Solution {
public:
    double myPow(double x, int n) {
        double power = 1;
        long m = n;
        if(m == 0){
            return 1;
        }
        
        if(m < 0){
            x = 1/x;
            m = -m;
        }

        while(m > 0){
            if(m%2){
                power *= x;
            }
            x *= x;
            m /= 2;
        }
        return power;
    }
};