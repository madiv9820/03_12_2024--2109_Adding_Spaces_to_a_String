# [2109. Adding Spaces to a String](https://leetcode.com/problems/adding-spaces-to-a-string?envType=daily-question&envId=2024-12-03)

__Type:__ Medium <br>
__Topics:__ Array, Two Pointers, String, Simulation <br>
__Companies:__ Google, Amazon, Meta
<hr>

You are given a **0-indexed** string `s` and a **0-indexed** integer array `spaces` that describes the indices in the original string where spaces will be added. Each space should be inserted **before** the character at the given index.

- For example, given `s = "EnjoyYourCoffee"` and `spaces = [5, 9]`, we place spaces before `'Y'` and `'C'`, which are at indices `5` and `9` respectively. Thus, we obtain `"Enjoy Your Coffee"`.

Return *the modified string ***after*** the spaces have been added.*
<hr>

### Examples

- **Example 1:** <br>
**Input:** s = "LeetcodeHelpsMeLearn", spaces = [8,13,15] <br>
**Output:** "Leetcode Helps Me Learn" <br>
**Explanation:** <br>
The indices 8, 13, and 15 correspond to the underlined characters in "Leetcode<u><b>H</b></u>elps<u><b>M</b></u>e<u><b>L</b></u>earn". <br>
We then place spaces before those characters.

- **Example 2:** <br>
**Input:** s = "icodeinpython", spaces = [1,5,7,9] <br>
**Output:** "i code in py thon" <br>
**Explanation:** <br>
The indices 1, 5, 7, and 9 correspond to the underlined characters in "i<u><b>c</b></u>ode<u><b>i</b></u>n<u><b>p</b></u>y<u><b>t</b></u>hon". <br>
We then place spaces before those characters.

- **Example 3:** <br> 
**Input:** s = "spacing", spaces = [0,1,2,3,4,5,6] <br>
**Output:** " s p a c i n g" <br>
**Explanation:** <br>
We are also able to place spaces before the first character of the string.
<hr>

### Constraints:
- <code>1 <= s.length <= 3 * 10<sup>5</sup></code>
- `s` consists only of lowercase and uppercase English letters.
- <code>1 <= spaces.length <= 3 * 10<sup>5</sup></code>
- `0 <= spaces[i] <= s.length - 1`
- All the values of `spaces` are **strictly increasing**.