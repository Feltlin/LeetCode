class Solution {
public:
    int binaryGap(int n) {
        int findOne = 0;
        int gap = 0;
        int maxGap = 0;
        while(n > 0){
            int digit = n % 2;
            n /= 2;
            findOne += digit;
            if((findOne == 1 && digit == 0) || findOne == 2){
                ++gap;
            }
            if(findOne == 2 && digit == 1){
                findOne = 1;
                if(gap > maxGap){
                    maxGap = gap;
                }
                gap = 0;
            }
        }
        return maxGap;

    //     int maxGap = 0;
    //     int gap = 0;
    //     int findOne = 0;
    //     while(n > 0){
    //         int remainder = n % 2;
    //         n /= 2;
    //         if(findOne == 1){
    //             gap += 1;
    //         }
    //         if(remainder){
    //             findOne += 1;
    //         }
    //         if(findOne == 2){
    //             findOne = 1;
    //             if(gap > maxGap){
    //                 maxGap = gap;
    //                 gap = 0;
    //             }
    //         }
    //     }
    //     return maxGap;
    }
};