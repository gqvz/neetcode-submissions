class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        map<pair<int, int>, int> visited{};
        auto m = grid.size();
        priority_queue<pair<int, pair<int, int>>> q{};
        // vector<pair<int, int>> ds{make_pair(0, 1), make_pair(0, -1), make_pair(1, 0), make_pair(-1, 0)};
        vector<pair<int, int>> ds{{0, 1},{0, -1}, {1, 0}, {-1, 0}};
        q.push({-grid[0][0], {0, 0}});
        while (!q.empty()) {
            auto [c, coords] = q.top();
            auto [i, j] = coords;
            q.pop();
            visited[{i, j}] = -c;
            if (i == m - 1 and j == m - 1) {
                break;
            }
            for (auto [di, dj] : ds) {
                auto ni = i + di;
                auto nj = j + dj;
                if (0 <= ni && ni < m && 0 <= nj && nj < m && !visited.contains({ni, nj})) {
                    q.push({-grid[nj][ni], {ni, nj}});
                }
            }
        }
        int max = 0;
        for (auto [p, v] : visited) {
            if (v > max){
                max = v;
            }
        }

        return max;
    }
};
