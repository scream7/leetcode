class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //num,index
        unordered_map<int, int> map;
        vector<int> result;
        for(int i = 0; i< nums.size();++i)
        {
            if(map.count(target - nums[i]) )
            {
                result.push_back(map[target - nums[i]] + 1);
                result.push_back(i+1);
                return result;
            }
            else
            {
                map[nums[i]] = i;
            }
        }
    }
};
