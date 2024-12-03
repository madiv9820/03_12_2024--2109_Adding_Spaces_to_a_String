from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Initialize the result string and the current word being built
        spacedString, currentWord = '', ''
        
        # spaceIndex is used to track the position of the next space index in the spaces list
        spaceIndex = 0
        
        # Get the length of the input string
        n = len(s)

        # Traverse through the string to process each character
        for index in range(n):
            # Check if the current index matches an index in the spaces list
            if spaceIndex < len(spaces) and index == spaces[spaceIndex]:
                # When a space index is found, add the current word followed by a space to the result
                spacedString += currentWord + ' '
                
                # Move to the next space index in the spaces list
                spaceIndex += 1
                
                # Reset currentWord to start collecting the next word
                currentWord = ''
            
            # Add the current character to the current word being built
            currentWord += s[index]

        # After finishing the loop, append the remaining word (there may be no space after the last word)
        spacedString += currentWord

        # Return the final string with spaces added
        return spacedString