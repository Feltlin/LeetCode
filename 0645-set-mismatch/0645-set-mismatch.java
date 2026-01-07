import java.util.Arrays;
class Solution {
    public int[] findErrorNums(int[] nums) {
        Arrays.sort(nums);
        int sum = nums.length * (nums.length + 1)/2;
        int[] number = {0, 0};
        for(int i = 0; i < nums.length; ++i){
            sum -= nums[i];
            if( i < nums.length - 1 && nums[i] == nums[i + 1]){
                number[0] = nums[i];
            }
        }
        number[1] = number[0] + sum;
        return number;
    }
}