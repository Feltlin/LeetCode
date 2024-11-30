class Solution {
    public int[] plusOne(int[] digits) {
        boolean carry = true;
        int i = digits.length - 1;
        while(carry){
            if(i >= 0){
                if(digits[i] == 9){
                    digits[i] = 0;
                }
                else{
                    ++digits[i];
                    carry = false;
                }
            }
            else{
                int[] newDigits = new int[digits.length + 1];
                newDigits[0] = 1;
                System.arraycopy(digits, 0, newDigits, 1, digits.length);
                digits = newDigits;
                carry = false;
            }
            --i;
        }
        return digits;
    }
}