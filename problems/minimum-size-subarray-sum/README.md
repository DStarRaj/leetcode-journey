# 209. Minimum Size Subarray Sum

[Link to LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)

Given an array of positive integers `nums` and a positive integer `target`, return _the **minimal length** of a [subarray](../../helper-docs/subarray.md) whose sum is greater than or equal to `target`_. If there is no such subarray, return `0` instead.

---

### Example 1:

<pre><code><strong>Input:</strong> target = 7, nums = [2,3,1,2,4,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The subarray [4,3] has the minimal length under the problem constraint.
</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> target = 4, nums = [1,4,4]
<strong>Output:</strong> 1</code></pre>

### Example 3:

<pre><code><strong>Input:</strong> target = 11, nums = [1,1,1,1,1,1,1,1]
<strong>Output:</strong> 0</code></pre>

### Constraints:

* <code>1 <= target <= 10<sup>9</sup></code>
* <code>1 <= nums.length <= 10<sup>5</sup></code>
* <code>1 <= nums[i] <= 10<sup>4</sup></code>

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.