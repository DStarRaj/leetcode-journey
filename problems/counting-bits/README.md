# 338. Counting Bits

[Link to LeetCode](https://leetcode.com/problems/counting-bits/description/)

Given an integer `n`, return _an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the **number of `1`'s** in the binary representation of `i`_.

---

### Example 1:

<pre><code><strong>Input:</strong> n = 2
<strong>Output:</strong> [0,1,1]
<strong>Explanation:</strong>
0 --> 0
1 --> 1
2 --> 10</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> n = 5
<strong>Output:</strong> [0,1,1,2,1,2]
<strong>Explanation:</strong>
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101</code></pre>

### Constraints:

* <code>0 <= n <= 10<sup>5</sup></code>

### Follow up:

* It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a single pass?
* Can you do it without using any built-in function (i.e., like `__builtin_popcount` in C++)?