# 167. Two Sum II - Input Array Is Sorted

[Link to LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

Given a **1-indexed** array of integers `numbers` that is already _**sorted in non-decreasing order**_, find two numbers such that they add up to a specific `target` number. Let these two numbers be <code>numbers[index<sub>1</sub>]</code> and <code>numbers[index<sub>2</sub>]</code> where <code>1 <= index<sub>1</sub> < index<sub>2</sub> < numbers.length</code>.

Return _the indices of the two numbers, <code>index<sub>1</sub></code> and <code>index<sub>2</sub></code>, **added by one** as an integer array <code>[index<sub>1</sub>, index<sub>2</sub>]</code> of length 2_.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

---

### Example 1:

<pre><code><strong>Input:</strong> numbers = [<ins>2</ins>,<ins>7</ins>,11,15], target = 9
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The sum of 2 and 7 is 9. Therefore, index<sub>1</sub> = 1, index<sub>2</sub> = 2. We return [1, 2].</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> numbers = [<ins>2</ins>,3,<ins>4</ins>], target = 6
<strong>Output:</strong> [1,3]
<strong>Explanation:</strong> The sum of 2 and 4 is 6. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 3. We return [1, 3].</code></pre>

### Example 3:

<pre><code><strong>Input:</strong> numbers = [<ins>-1</ins>,<ins>0</ins>], target = -1
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> The sum of -1 and 0 is -1. Therefore index<sub>1</sub> = 1, index<sub>2</sub> = 2. We return [1, 2].</code></pre>

### Constraints:

* <code>2 <= numbers.length <= 3 * 10<sup>4</sup></code>
* `-1000 <= numbers[i] <= 1000`
* `numbers` is sorted in **non-decreasing order**.
* `-1000 <= target <= 1000`
* The tests are generated such that there is **exactly one solution**.