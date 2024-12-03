# Adding Spaces to a String using Two Pointers
- ### Intuition:
    The goal of this problem is to insert spaces into a string `s` at specified indices given in the `spaces` array. The strategy is to traverse through the string character by character while checking if the current index matches any of the indices in the `spaces` list. If it does, we append the current word followed by a space to the result string. We continue building words as we traverse the string, adding spaces where required.

- ### Approach:
    1. **Initialization**:
        - Initialize an empty string `spacedString` to accumulate the result with spaces added.
        - Initialize a `currentWord` string to collect characters of each word as we process the string.
        - Use a `spaceIndex` to keep track of the next space index in the `spaces` array.

    2. **Traverse through the string**:
        - For each character in the string `s`, check if the current index matches an index from the `spaces` array.
        - If the index matches, append the `currentWord` followed by a space to `spacedString`, and reset `currentWord` to start building the next word.
        - Continue to add characters to `currentWord` as you progress through the string.

    3. **Post-loop**:
        - After the loop finishes, append any remaining characters in `currentWord` to `spacedString` (this is necessary as the loop may end without encountering a space index).

    4. **Return**:
        - Return the `spacedString`, which is the original string with spaces inserted at the correct positions.

- ### Time Complexity:
    - **O(n)**: We traverse the string `s` once, where `n` is the length of the string. Each operation inside the loop (checking the condition, appending characters) is done in constant time.

- ### Space Complexity:
    - **O(n)**: We use additional space for storing `spacedString` and `currentWord`. In the worst case, where no spaces are added, `spacedString` will be of length `n`. Thus, the space complexity is proportional to the size of the string.