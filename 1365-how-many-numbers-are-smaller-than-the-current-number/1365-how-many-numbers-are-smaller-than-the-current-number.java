import java.util.Arrays;
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] numsCopy = Arrays.copyOf(nums, nums.length);
        Arrays.sort(numsCopy);
        for(int i = 0; i < nums.length; ++i){
            int count = 0;
            for(int j = 0; j < nums.length; ++j){
                if(numsCopy[j] < nums[i]){
                    ++count;
                }
            }
            nums[i] = count;
        }
        return nums;
    }
}