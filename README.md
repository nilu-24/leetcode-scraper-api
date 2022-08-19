# leetcode-scraper-api


REST API built with Flask and bs4 which scrapes and fetches questions from LeetCode. 
Response is a JSON object containing information about question title, difficulty, Id, and HTML content, including images directly scraped from LeetCode.

Use LeetCode Problem Tag:

Example: For the problem url https://leetcode.com/problems/trapping-rain-water/, the Problem Tag is **trapping-rain-water**

API request: https://leetcode-scraper-api.herokuapp.com/?question=trapping-rain-water

API response: 

```json
{
"difficulty": "Hard",
"question": "<p>Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is <code>1</code>, compute how much water it can trap after raining.</p> <p> </p> <p><strong>Example 1:</strong></p> <img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" style="width: 412px; height: 161px;"/> <pre> <strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1] <strong>Output:</strong> 6 <strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. </pre> <p><strong>Example 2:</strong></p> <pre> <strong>Input:</strong> height = [4,2,0,3,2,5] <strong>Output:</strong> 9 </pre> <p> </p> <p><strong>Constraints:</strong></p> <ul> <li><code>n == height.length</code></li> <li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li> <li><code>0 &lt;= height[i] &lt;= 10<sup>5</sup></code></li> </ul> ",
"questionId": "42",
"title": "Trapping Rain Water"
}

```


<p>Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is <code>1</code>, compute how much water it can trap after raining.</p> <p> </p> <p><strong>Example 1:</strong></p> <img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" style="width: 412px; height: 161px;"/> <pre> <strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1] <strong>Output:</strong> 6 <strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. </pre> <p><strong>Example 2:</strong></p> <pre> <strong>Input:</strong> height = [4,2,0,3,2,5] <strong>Output:</strong> 9 </pre> <p> </p> <p><strong>Constraints:</strong></p> <ul> <li><code>n == height.length</code></li> <li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li> <li><code>0 &lt;= height[i] &lt;= 10<sup>5</sup></code></li> </ul>

