# Time Complexity

| Scenario | Time Complexity | Description |
| :--- | :--- | :--- |
| Best Case | O(n³) | The algorithm uses three nested loops to test every split point for all sub-chains, regardless of input values. |
| Average Case | O(n³) | It systematically computes and compares multiplication costs for all possible parenthesizations. |
| Worst Case | O(n³) | The split point `k` must always iterate from `i` to `j - 1` across all matrix sub-chains. |

# Space Complexity

| Approach | Space Complexity | Description |
| :--- | :--- | :--- |
| 2D Table Approach | O(n²) | Allocates an (n + 1) × (n + 1) matrix to store the minimum scalar multiplication costs for the sub-chains. |

# Conclusion

The Matrix Chain Multiplication problem solved using Dynamic Programming guarantees a time complexity of **O(n³)** due to its three nested loops: one for chain length, one for the starting index, and one for the partition split point. Its space complexity is **O(n²)** to hold the complete cost grid.
