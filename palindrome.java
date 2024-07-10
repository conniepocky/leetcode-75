class Solution {
    public boolean isPalindrome(String s) {
        String str = s.replaceAll("[^a-zA-Z0-9]+", "").toLowerCase();

        char[] arr = str.toCharArray();

        int low = 0;
        int high = str.length()-1;

        while (low < high) {
            if (arr[low] == arr[high]) {
                low ++;
                high --;
            } else {
                return false;
            }
        }

        return true;
    }
}
