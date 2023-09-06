# 141. Linked List Cycle

[Link to LeetCode](https://leetcode.com/problems/linked-list-cycle/)

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return _`true` if there is a cycle in the linked list_. Otherwise, return `false`.

---

### Example 1:

![Illustration of graph](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

<pre><code><strong>Input:</strong> head = [3,2,0,-4], pos = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).</code></pre>

### Example 2:

![Illustration of graph](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

<pre><code><strong>Input:</strong> head = [1,2], pos = 0
<strong>Output:</strong> true
<strong>Explanation:</strong> There is a cycle in the linked list, where the tail connects to the 0th node.</code></pre>

### Example 3:

![Illustration of graph](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

<pre><code><strong>Input:</strong> head = [1], pos = -1
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no cycle in the linked list.</code></pre>

### Constraints:

* The number of the nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.
* <code>-10<sup>5</sup> <= Node.val <= 10<sup>5</sup></code>
* `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?