# 9. Palindrome Number

[Link to LeetCode](https://leetcode.com/problems/palindrome-number/)

Given an integer `x`, return `true` if `x` is a [palindrome](../../helper-docs/palindrome.md), and `false` otherwise.

---

### Example 1:

<pre><code><strong>Input:</strong> x = 121
<strong>Output:</strong> true
<strong>Explanation:</strong> 121 reads as 121 from left to right and from right to left.</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.</code></pre>

### Example 3:

<pre><code><strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.</code></pre>

### Constraints:

* <code>-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1</code>
 

<strong>Follow up:</strong> Could you solve it without converting the integer to a string?