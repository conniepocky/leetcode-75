#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max = *max_element(candies.begin(), candies.end());

        vector <bool> result(candies.size());

        int i;

        for (i = 0; i < candies.size(); i++) {
            result[i] = (candies[i]+extraCandies >= max);
        }

        return result;
    }
};



