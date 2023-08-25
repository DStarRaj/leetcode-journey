# 97. Interleaving String

[Link to LeetCode](https://leetcode.com/problems/interleaving-string/)

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an **interleaving** of `s1` and `s2`.

An **interleaving** of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` [substrings](../../helper-docs/substring.md) respectively, such that:

* <code>s = s<sub>1</sub> + s<sub>2</sub> + ... + s<sub>n</sub></code>
* <code>t = t<sub>1</sub> + t<sub>2</sub> + ... + t<sub>m</sub></code>
* `|n - m| <= 1`
* The **interleaving** is <code>s<sub>1</sub> + t<sub>1</sub> + s<sub>2</sub> + t<sub>2</sub> + s<sub>3</sub> + t<sub>3</sub> + ...</code> or <code>t<sub>1</sub> + s<sub>1</sub> + t<sub>2</sub> + s<sub>2</sub> + t<sub>3</sub> + s<sub>3</sub> + ...</code>

**Note:** `a + b` is the concatenation of strings `a` and `b`.

---

### Example 1:

![Illustration of interleaving](https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg)

<pre><code><strong>Input:</strong> s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
<strong>Output:</strong> true
<strong>Explanation:</strong> One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
<strong>Output:</strong> false
<strong>Explanation:</strong> Notice how it is impossible to interleave s2 with any other string to obtain s3.</code></pre>

### Example 3:

<pre><code><strong>Input:</strong> s1 = "", s2 = "", s3 = ""
<strong>Output:</strong> true</code></pre>

### Constraints:

* `0 <= s1.length, s2.length <= 100`
* `0 <= s3.length <= 200`
* `s1`, `s2`, and `s3` consist of lowercase English letters

**Follow up:** Could you solve it using only `O(s2.length)` additional memory space?