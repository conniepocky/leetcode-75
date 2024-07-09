class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int rows = maze.size(), cols = maze[0].size();

        queue<vector<int>> queue{{entrance}};
        vector<int> directions = {-1, 0, 1, 0, -1};

        maze[entrance[0]][entrance[1]] = '+'; //mark as visited

        int steps = 0;

        while (!queue.empty()) {
            steps ++;

            for (int count = queue.size(); count > 0; --count) {
                auto pos = queue.front();
                queue.pop();

                for (int i = 0; i < 4; i++) {
                    int x = pos[0] + directions[i];
                    int y = pos[1] + directions[i + 1];

                    if (x >= 0 && x < rows && y >= 0 && y < cols && maze[x][y] == '.') {
                        if (x == 0 || x == rows-1 || y == 0 || y == cols-1) {
                            return steps;
                        }

                        queue.push({x,y});
                        maze[x][y] = '+';
                    }
                }
            }
        }

        return -1;

    }
};
