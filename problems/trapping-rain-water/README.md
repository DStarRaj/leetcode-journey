# 42. Trapping Rain Water

[Link to LeetCode](https://leetcode.com/problems/trapping-rain-water/)

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

---

### Example 1:

![Illustration of rain](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

<pre><code><strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> height = [4,2,0,3,2,5]
<strong>Output:</strong> 9</code></pre>

### Constraints:

* `n == height.length`
* <code>1 <= n <= 2 * 10<sup>4</sup></code>
* <code>0 <= height[i] <= 10<sup>5</sup></code>