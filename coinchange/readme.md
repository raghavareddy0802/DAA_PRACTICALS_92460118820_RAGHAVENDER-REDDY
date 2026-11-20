# Time Complexity

| Scenario | Time Complexity | Description |
| :--- | :--- | :--- |
| Best Case | O(n × amount) | The algorithm must always fill the entire 2D table regardless of coin values. |
| Average Case | O(n × amount) | Every cell in the grid requires a constant time check to find the minimum coins. |
| Worst Case | O(n × amount) | The loops run through all coin denominations and all amount increments every single time. |

# Space Complexity

| Approach | Space Complexity | Description |
| :--- | :--- | :--- |
| 2D Grid Approach | O(n × amount) | Allocates an (n + 1) × (amount + 1) matrix to store intermediate sub-problems. |

# Conclusion

The Coin Change problem solved via a 2D Dynamic Programming matrix guarantees a time complexity of **O(n × amount)** (where *n* is the number of coin denominations) because it systematically evaluates every coin against every sub-amount. The space complexity is **O(n × amount)** to hold the complete grid state.
