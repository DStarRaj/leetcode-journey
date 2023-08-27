# 238. Product of Array Except Self

[Link to LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

Given an integer array `nums`, return _an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`_.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

---

### Example 1:

<pre><code><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]</code></pre>

### Constraints:

* <code>2 <= nums.length <= 10<sup>5</sup></code>
* `-30 <= nums[i] <= 30`
* The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.


<strong>Follow up:</strong> Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)