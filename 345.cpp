class Solution {

private:
    const string vowels_ = "aeiou";
    bool is_vowel(char a){
        return vowels_.find(a) != string::npos;
    }

public:
    string reverseVowels(string s) {
       int left = 0;
       int right = s.size();

       while (left < right) {
            if (!is_vowel(tolower(s[left]))) {
                ++left;
            } else if (!is_vowel(tolower(s[right]))) {
                --right;
            } else {
                swap(s[left++], s[right--]);
            }
       }
       return s;
    }
};
