class Solution:

  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    st = 0
    e = len(numbers) - 1

    while st < e:
      current_sum = numbers[st] + numbers[e]

      if current_sum == target:
        # Note: LeetCode 167 is 1-indexed, so we return [st + 1, e + 1]
        return [st + 1, e + 1]
      elif current_sum < target:
        st += 1  # We need a larger sum, move left pointer right
      else:
        e -= 1  # We need a smaller sum, move right pointer left

    return []