class Solution {
public:
    int tribonacci(int n) {

        if (n == 0) {
            return 0;
        } else if (n < 3) {
            return 1;
        }

        int a = 0, b = 1, c = 1;

        for (int i = 2; i < n; i++) {
            int newVal = a+b+c;

            a = b;
            b = c;
            c = newVal;
        }

        return c;
    }
};
