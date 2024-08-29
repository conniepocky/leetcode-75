public class Solution {
    public int PivotIndex(int[] nums) {
        int r = nums.Sum();
        int l = 0;
        for (int i = 0; i < nums.Length; i++) {
            r -= nums[i];

            if (r == l) {
                return i;
            }

            l += nums[i];
        }

        return -1;
    }
}
