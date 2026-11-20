# Time Complexity

| Scenario | Time Complexity | Description |
| :--- | :--- | :--- |
| Best Case | O(n log n) | Pivot divides the array into nearly equal parts |
| Average Case | O(n log n) | The array is divided into smaller parts efficiently |
| Worst Case | O(n²) | Pivot creates highly unbalanced partitions |

# Space Complexity

| Space Complexity |
| :--- |
| O(n) |

# Conclusion

Quick Sort works by selecting a pivot and dividing the elements into smaller and larger parts. It then recursively sorts these parts. Its best-case and average-case time complexity is **O(n log n)**, while its worst-case time complexity is **O(n²)**. For this implementation, the space complexity is **O(n)**.