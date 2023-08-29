# 2483. Minimum Penalty for a Shop

[Link to LeetCode](https://leetcode.com/problems/minimum-penalty-for-a-shop/)

You are given the customer visit log of a shop represented by a **0-indexed** string `customers` consisting only of characters `'N'` and `'Y'`:

* if the <code>i<sup>th</sup></code> character is `'Y'`, it means that customers come at the <code>i<sup>th</sup></code> hour
* whereas `'N'` indicates that no customers come at the <code>i<sup>th</sup></code> hour.

If the shop closes at the <code>j<sup>th</sup></code> hour `(0 <= j <= n)`, the **penalty** is calculated as follows:

* For every hour when the shop is open and no customers come, the penalty increases by `1`.
* For every hour when the shop is closed and customers come, the penalty increases by `1`.

Return _the **earliest** hour at which the shop must be closed to incur a **minimum** penalty_.

**Note** that if a shop closes at the <code>j<sup>th</sup></code> hour, it means the shop is closed at the hour `j`.

---

### Example 1:

<pre><code><strong>Input:</strong> customers = "YYNY"
<strong>Output:</strong> 2
<strong>Explanation:</strong>
- Closing the shop at the 0<sup>th</sup> hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1<sup>st</sup> hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2<sup>nd</sup> hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3<sup>rd</sup> hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4<sup>th</sup> hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2<sup>nd</sup> or 4<sup>th</sup> hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> customers = "NNNNN"
<strong>Output:</strong> 0
<strong>Explanation:</strong> It is best to close the shop at the 0<sup>th</sup> hour as no customers arrive.</code></pre>

### Example 3:

<pre><code><strong>Input:</strong> customers = "YYYY"
<strong>Output:</strong> 4
<strong>Explanation:</strong> It is best to close the shop at the 4<sup>th</sup> hour as customers arrive at each hour.</code></pre>

### Constraints:

* <code>1 <= customers.length <= 10<sup>5</sup></code>
* `customers` consists only of characters `'Y'` and `'N'`.