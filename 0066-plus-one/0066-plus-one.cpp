class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool carry = true;
        int i = digits.size() - 1;
        while(carry){
            if (i >= 0){
                if(digits[i] == 9){
                    digits[i] = 0;
                }
                else{
                    digits[i] += 1;
                    carry = false;
                }
            }
            else{
                digits.insert(digits.begin(), 1);
                carry = false;
            }
            --i;
        }
        return digits;
    }
};