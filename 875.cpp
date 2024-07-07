class Solution {
public:
    bool canEat(vector<int>& piles, int speed, int h) {
        int hours = 0;

        for (int p: piles) {
            hours += p / speed;
            if (p % speed != 0) {
                hours ++;
            }
        }
        return hours <= h;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *max_element(piles.begin(),piles.end());
        int ans;

        while (left <= right) {
            int mid = (left+right) / 2;

            if (canEat(piles, mid, h)) {
                ans = mid;
                right = mid-1;
            } else {
                left = mid+1;
            }
        }

        return ans;
    }
};
