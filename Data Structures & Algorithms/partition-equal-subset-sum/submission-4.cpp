class Solution {
public:
    bool dfs(int cur, vector<int>::iterator i, const vector<int> &nums, const int hs, map<pair<int, vector<int>::iterator>, bool>& memo) {
        if (cur == hs) return true;
        if (cur > hs || i == nums.end()) return false;
        if (memo.contains({cur, i})) return memo[{cur, i}];
        if (dfs(cur+*i, i+1, nums, hs, memo) || dfs(cur, i+1, nums, hs, memo) ) return true;
        memo[{cur, i}] = false;
        return false;
    }
    bool canPartition(vector<int>& nums) {
        int sum = std::accumulate(nums.begin(), nums.end(), 0);
        if (sum % 2 == 1) return false;
        int hs = sum / 2;
        map<pair<int, vector<int>::iterator>, bool> memo;
        return dfs(0, nums.begin(), nums, hs, memo);
    }
};
