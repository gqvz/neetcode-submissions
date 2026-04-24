class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        multiset<int> cs;
        for (int i = 0; i < k-1; i++){
            cs.insert(nums[i]);
        }

        vector<int> res(nums.size() - k + 1);
        for (int i = k-1; i < nums.size(); i++){
            cs.insert(nums[i]);
            res[i-k+1] = *cs.rbegin();
            cs.erase(cs.find(nums[i-k+1]));
        }
        return res;
    }
};
