# Time Complexity

| Scenario | Time Complexity | Description |
| :--- | :--- | :--- |
| Best Case | O(n × capacity) | The algorithm must always fill the entire 2D table regardless of item values. |
| Average Case | O(n × capacity) | Every cell in the grid requires a constant time check to compute the maximum profit. |
| Worst Case | O(n × capacity) | The loops run through all items and all capacity increments every single time. |

# Space Complexity

| Approach | Space Complexity | Description |
| :--- | :--- | :--- |
| Your 2D Code | O(n × capacity) | Allocates an (n + 1) × (capacity + 1) matrix to store intermediate results. |
| Optimized 1D Code | O(capacity) | Reduces the memory footprint by keeping track of only the current capacity states. |

# Conclusion

The 0/1 Knapsack problem solved via Dynamic Programming guarantees a time complexity of **O(n × capacity)** because it systematically evaluates every item against every weight capacity. While your original 2D matrix approach utilizes **O(n × capacity)** space, it can be optimized down to a space complexity of **O(capacity)** by utilizing a single 1D array.
