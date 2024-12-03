#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        // Initialize the result string to accumulate the final spaced string
        string spacedString = "", currentWord = "";
        
        // Initialize spaceIndex to keep track of the next space index to add
        int spaceIndex = 0;
        
        // Get the length of the input string
        int n = s.length();

        // Traverse through the string character by character
        for(int index = 0; index < n; ++index) {
            // If the current index matches an index in the spaces array
            if(spaceIndex < spaces.size() && index == spaces[spaceIndex]) {
                // Add the current word to spacedString followed by a space
                spacedString += (currentWord + ' ');
                
                // Reset currentWord to start building the next word
                currentWord = "";
                
                // Move to the next space index in the spaces list
                ++spaceIndex;
            }

            // Add the current character to the current word
            currentWord += s[index];
        }

        // Append the last remaining word (there may be no space after the last word)
        spacedString += currentWord;

        // Return the final string with spaces inserted
        return spacedString;
    }
};

int main() {
    string s = "LeetcodeHelpsMeLearn"; vector<int> spaces = {8,13,15}; Solution sol;
    cout << sol.addSpaces(s, spaces) << endl;
}