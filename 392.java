class Solution {
    public boolean isSubsequence(String s, String t) {

        int sNum = 0;
        int tNum = 0;

        int total = 0;

        while (sNum < s.length() && tNum < t.length()) {
            if (s.charAt(sNum) == t.charAt(tNum)) {
                total ++;
                sNum ++;
            }
            tNum ++;
        }

        return (total == s.length());
    }
}
