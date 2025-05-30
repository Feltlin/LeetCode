import java.lang.Math;
class Solution {
    public int reverse(int x) {
        int y = 0;
        while(x != 0){
            if(Math.abs(y) > Math.pow(2, 31) / 10){
                return 0;
            }
            y =  y * 10 + x % 10;
            x /= 10;
        }
        return y;
    }
}