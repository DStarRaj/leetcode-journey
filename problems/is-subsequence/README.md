# 392. Is Subsequence

[Link to LeetCode](https://leetcode.com/problems/is-subsequence/)

Given two strings `s` and `t`, return _`true` if `s` is a **subsequence** of `t`, or `false` otherwise_.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of <code>"<ins>a</ins>b<ins>c</ins>d<ins>e</ins>"</code> while `"aec"` is not).

---

### Example 1:

<pre><code><strong>Input:</strong> s = "abc", t = "ahbgdc"
<strong>Output:</strong> true</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> s = "axc", t = "ahbgdc"
<strong>Output:</strong> false</code></pre>

### Constraints:

* `0 <= s.length <= 100`
* <code>0 <= t.length <= 10<sup>4</sup></code>
* `s` and `t` consist only of lowercase English letters.

**Follow up:** Suppose there are lots of incoming `s`, say <code>s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub></code> where <code>k >= 10<sup>9</sup></code>, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?