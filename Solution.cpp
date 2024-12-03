#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string spacedString = "",  currentWord = "";
        int spaceIndex = 0, n = s.length();

        for(int index = 0; index < n; ++index) {
            if(spaceIndex < spaces.size() && index == spaces[spaceIndex]) {
                spacedString += (currentWord + ' ');
                currentWord = "";
                ++spaceIndex;
            } 

            currentWord += s[index];
        }

        spacedString += currentWord;

        return spacedString;
    }
};

int main() {
    string s = "LeetcodeHelpsMeLearn"; vector<int> spaces = {8,13,15}; Solution sol;
    cout << sol.addSpaces(s, spaces) << endl;
}