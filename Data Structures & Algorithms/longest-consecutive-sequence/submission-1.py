from typing import List


class Solution:

  def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0

    streak_map = {}  # Stores the length of the sequence touching this number
    longest = 0

    for num in nums:
        # If the number is already part of a sequence, skip it
        if num in streak_map:
            continue

        # Get lengths of adjacent sequences (default to 0 if not present)
        left = streak_map.get(num - 1, 0)
        right = streak_map.get(num + 1, 0)

        # Total length of the new merged sequence
        current_length = left + right + 1
        longest = max(longest, current_length)

        # Store the current number's length
        streak_map[num] = current_length

        # Update the boundaries of the combined sequence
        # Left boundary is (num - left), right boundary is (num + right)
        streak_map[num - left] = current_length
        streak_map[num + right] = current_length

    return longest