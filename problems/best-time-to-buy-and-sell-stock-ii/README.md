# 122. Best Time to Buy and Sell Stock II

[Link to LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the <code>i<sup>th</sup></code> day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can buy it then immediately sell it on the **same day**.

Find and return _the **maximum** profit you can achieve_.

---

### Example 1:

<pre><code><strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.</code></pre>

### Example 2:

<pre><code><strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.</code></pre>

### Example 3:

<pre><code><strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.</code></pre>

### Constraints:

* <code>1 <= prices.length <= 3 * 10<sup>4</sup></code>
* <code>0 <= prices[i] <= 10<sup>4</sup></code>