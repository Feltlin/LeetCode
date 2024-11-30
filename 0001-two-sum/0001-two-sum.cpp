class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); ++i){
            int a = nums.at(i);
            for (int j = i+1; j < nums.size(); ++j){
                int b = nums.at(j);
                if (a + b == target){
                    return vector<int>({i,j});
                }
            }
        }
        return vector<int>();
    }
};