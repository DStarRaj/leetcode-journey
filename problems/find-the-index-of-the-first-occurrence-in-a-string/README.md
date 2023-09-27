# 28. Find the Index of the First Occurrence in a String

[Link to LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

---

### Example 1:

<pre><code><strong>Input:</strong> haystack = "sadbutsad", needle = "sad"
<strong>Output:</strong> 0
<strong>Explanation:</strong> "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> haystack = "leetcode", needle = "leeto"
<strong>Output:</strong> -1
<strong>Explanation:</strong> "leeto" did not occur in "leetcode", so we return -1.</code></pre>

### Constraints:

* <code>1 <= haystack.length, needle.length <= 10<sup>4</sup></code>
* `haystack` and `needle` consist of only lowercase English characters.