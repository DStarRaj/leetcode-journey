# 125. Valid Palindrome

[Link to LeetCode](https://leetcode.com/problems/valid-palindrome/)

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return _`true` if it is a **palindrome**, or `false` otherwise_.

---

### Example 1:

<pre><code><strong>Input:</strong> s = "A man, a plan, a canal: Panama"
<strong>Output:</strong> true
<strong>Explanation:</strong> "amanaplanacanalpanama" is a palindrome.</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> s = "race a car"
<strong>Output:</strong> false
<strong>Explanation:</strong> "raceacar" is not a palindrome.</code></pre>

### Example 3:

<pre><code><strong>Input:</strong> s = " "
<strong>Output:</strong> true
<strong>Explanation:</strong> s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.</code></pre>

### Constraints:

* <code>1 <= s.length <= 2 * 10<sup>5</sup></code>
* `s` consists only of printable ASCII characters.