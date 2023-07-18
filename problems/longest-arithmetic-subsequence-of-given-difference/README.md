# 1218. Longest Arithmetic Subsequence of Given Difference

[Link to LeetCode](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/)

Given an integer array `arr` and an integer `difference`, return the length of the longest subsequence in `arr` which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals `difference`.

A **subsequence** is a sequence that can be derived from `arr` by deleting some or no elements without changing the order of the remaining elements.

---

### Example 1:

<pre><code><strong>Input:</strong> arr = [1,2,3,4], difference = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest arithmetic subsequence is [1,2,3,4].</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> arr = [1,3,5,7], difference = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> The longest arithmetic subsequence is any single element.</code></pre>

### Example 3:

<pre><code><strong>Input:</strong> arr = [1,5,7,8,5,3,4,2,1], difference = -2
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest arithmetic subsequence is [7,5,3,1].</code></pre>

### Constraints:

* <code>1 <= arr.length <= 10<sup>5</sup></code>
* <code>-10<sup>4</sup> <= arr[i], difference <= 10<sup>4</sup></code>
