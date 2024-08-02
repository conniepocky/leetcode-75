public class Solution {
    public bool IncreasingTriplet(int[] nums) {
        int f = int.MaxValue;
        int s = int.MaxValue;

        for (int idx = 0; idx < nums.Length; idx++) {
            if (nums[idx] <= f) {
                f = nums[idx];
            } else if (nums[idx] <= s) {
                s = nums[idx];
            } else {
                return true;
            }
        }
        return false;
    }
}
