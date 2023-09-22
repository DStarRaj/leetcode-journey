# 287. Find the Duplicate Number

[Link to LeetCode](https://leetcode.com/problems/find-the-duplicate-number/)

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return _this repeated number_.

You must solve the problem **without** modifying the array `nums` and uses only constant extra space.

---

### Example 1:

<pre><code><strong>Input:</strong> nums = [1,3,4,2,2]
<strong>Output:</strong> 2</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> nums = [3,1,3,4,2]
<strong>Output:</strong> 3</code></pre>

### Constraints:

* <code>1 <= n <= 10<sup>5</sup></code>
* `nums.length == n + 1`
* `1 <= nums[i] <= n`
* All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

### Follow up:

* How can we prove that at least one duplicate number must exist in `nums`?
* Can you solve the problem in linear runtime complexity?