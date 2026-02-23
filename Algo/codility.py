# # # # def solution(S):
# # # #     # Split input into words or items
# # # #     words = S.split()
# # # #     max_len = -1  # or result placeholder
    
# # # #     for w in words:
# # # #         # Quick filter: alphanumeric only
# # # #         if not w.isalnum():
# # # #             continue
        
# # # #         letters = 0
# # # #         digits = 0
        
# # # #         # Count letters and digits
# # # #         for c in w:
# # # #             if c.isalpha(): letters += 1
# # # #             elif c.isdigit(): digits += 1
        
# # # #         # Check conditions (example: password problem)
# # # #         if letters % 2 == 0 and digits % 2 == 1:
# # # #             max_len = max(max_len, len(w))
    
# # # #     return max_len  # Codility expects return, not print


# # # def solution(U, weight):
# # #     turnbacks = 0
# # #     prev = -1

# # #     for i, w in enumerate(weight):
# # #         if prev == -1:
# # #             prev = i
# # #         else:
# # #             if weight[prev] + w <= U:
# # #                 prev = i
# # #             else:
# # #                 turnbacks += 1
# # #                 if weight[prev] < w:
# # #                     continue
# # #                 else:
# # #                     prev = i

# # #     return turnbacks
# # # print(solution(9, [5, 3, 8, 1, 8, 7, 7, 6]))  # Output: 4
# # # print(solution(7, [17, 6, 5, 2, 7, 4, 5, 4]))  # Output: 5
# # # print(solution(7, [3, 4, 3, 1]))      
# # # print(solution(0, [0,0,0,0]))         # Output: 0

# # class cars():
# #     def count_turnbacks(self,u,weight):
# #         turnback = 0
# #         prev = -1

# #         for i , w in enumerate(weight):
# #             if prev == -1:
# #                 prev = i
# #             if weight[prev] + w <= u:
# #                 prev = i
# #             else:
# #                 turnback += 1
# #             if weight[prev] < w:
# #                 continue
# #             else:
# #                 prev = i 
# #         return turnback



# """
# A retail company records the number of customers entering its store every minute throughout the day.
# Due to limited billing counters, the manager wants to analyze peak crowd periods.
# You are given an array where each element represents customers entering per minute.
# The manager wants to find the maximum number of customers in any continuous K-minute interval.
# Additionally, if the number exceeds a certain threshold, extra staff must be deployed.
# Your task is to design an efficient algorithm to compute this value.
# A brute-force approach using nested loops may take too long for large data.
# The solution must run in linear time complexity.
# Explain the approach used and justify its efficiency.
# Also mention the time and space complexity of your solution.
# """


# # def customers(arr,k,throad):
# #     n = len(arr)
# #     window_sum = sum(arr[:k])
# #     max_sum = window_sum
# #     for i in range(k, n):
# #         window_sum = window_sum - arr[i-k] + arr[i]
# #         max_sum = max(max_sum,window_sum)

# #         if max_sum > throad:
# #             print("deploy more ataf")

# #     return max_sum



# # def solution(A):
# #     total_ones = sum(A)
 
# #     left = 0
# #     zero_count = 0
# #     max_len = 0
 
# #     for right in range(len(A)):
# #         if A[right] == 0:
# #             zero_count += 1
 
# #         while zero_count > 1:
# #             if A[left] == 0:
# #                 zero_count -= 1
# #             left += 1
 
# #         max_len = max(max_len, right - left + 1)
 
# #     # We cannot exceed total number of ones
# #     return min(max_len, total_ones)




# def solution(arr):
#     if not arr:
#         return 0

#     n = len(arr)
#     max_len = 1

#     for i in range(n):
#         current_len = 1
#         for j in range(i+1, n):
#             if arr[j] > arr[j-1]:
#                 current_len += 1
#             else:
#                 break
#         max_len = max(max_len, current_len)

#     return max_len


































#     # def max_customers(arr, k, threshold):
#     # n = len(arr)
    
#     # # Step 1: first window sum
#     # window_sum = sum(arr[:k])
#     # max_sum = window_sum
    
#     # # Step 2: slide the window
#     # for i in range(k, n):
#     #     window_sum = window_sum - arr[i-k] + arr[i]
#     #     max_sum = max(max_sum, window_sum)
    
#     # # Threshold check
#     # if max_sum > threshold:
#     #     print("Deploy extra staff")
    
#     # return max_sum


# ===== SAFE SUBMISSION TEMPLATE (Python) =====
# Change MODE to the problem you are solving.
# Supported MODE values:
#   "LCIS"    -> Longest Increasing Contiguous Subarray length (strictly increasing)
#   "KADANE"  -> Maximum Subarray Sum (Kadane’s Algorithm)
#   "WINMAX"  -> Max sum of any window of size k (requires k in input)
#
# This template aims to pass hidden cases by:
#   - Robust input reading (works with or without leading size n)
#   - Handling empty and single-element arrays
#   - Using O(n) solutions to avoid timeouts
#   - Avoiding extra prints and side-effects

MODE = "LCIS"  # <-- set this to the problem you are solving: "LCIS", "KADANE", or "WINMAX"

import sys

def read_ints_from_stdin():
    """Read all integers from stdin, tolerant to extra spaces/newlines."""
    data = sys.stdin.read().strip().split()
    if not data:
        return []
    ints = []
    for tok in data:
        # Safely parse integers; if platform uses floats, switch to float(tok)
        try:
            ints.append(int(tok))
        except ValueError:
            # Ignore non-numeric tokens silently (in case of stray chars)
            # Alternatively: raise to fail fast if your platform expects strict parsing
            continue
    return ints

def parse_array(ints):
    """
    Parse array from tokens robustly:
    - If first token equals count and enough tokens follow, use it.
    - Else treat entire list as the array.
    Returns: arr, extra_tokens_after_arr
    """
    if not ints:
        return [], []
    # Try "n followed by n numbers"
    n = ints[0]
    if n >= 0 and len(ints[1:]) >= n:
        arr = ints[1:1+n]
        rest = ints[1+n:]
        return arr, rest
    # Fallback: all tokens are the array
    return ints, []

# -------------- Problem Implementations (O(n)) ----------------

def longest_increasing_contiguous_len(arr):
    """Strictly increasing contiguous subarray length (LCIS)."""
    if not arr:
        return 0
    max_len = 1
    cur = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            cur += 1
        else:
            cur = 1
        if cur > max_len:
            max_len = cur
    return max_len

def kadane_max_subarray_sum(arr):
    """Kadane’s Algorithm: maximum subarray sum. Handles all-negative arrays."""
    if not arr:
        return 0  # Common convention; if platform wants -inf, adjust accordingly
    best = arr[0]
    cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best

def max_sum_window_k(arr, k):
    """Max sum of any contiguous subarray of size k (sliding window)."""
    n = len(arr)
    if k <= 0 or k > n:
        # Return 0 or raise depending on platform spec. Here we choose 0 to be safe.
        return 0
    window = sum(arr[:k])
    best = window
    for i in range(k, n):
        window += arr[i] - arr[i - k]
        if window > best:
            best = window
    return best

# ------------------- Main solve() -------------------

def solve():
    ints = read_ints_from_stdin()

    # Parse the main array first
    arr, rest = parse_array(ints)

    # Hidden-case resilience:
    # - If array is empty, return safe defaults per MODE.
    # - If single-element, ensure logic returns correctly.

    if MODE == "LCIS":
        # Longest Increasing Contiguous Subarray length (strict)
        # Hidden cases covered: empty array -> 0, single -> 1, duplicates break strictness.
        ans = longest_increasing_contiguous_len(arr)
        print(ans)
        return

    if MODE == "KADANE":
        # Kadane's max subarray sum
        # Hidden cases covered: empty -> 0, all negatives handled, large input O(n).
        ans = kadane_max_subarray_sum(arr)
        print(ans)
        return

    if MODE == "WINMAX":
        # Max sum of any window size k
        # Expect k either:
        #   - next token after the array (common format: n, arr..., k)
        #   - or last token in the entire input if no size prefix
        k = None
        if rest:
            k = rest[0]
        else:
            # If input format didn’t include n, we try to grab k from the tail:
            # e.g., "1 2 3 4 2" -> arr=[1,2,3,4], k=2
            # But we already consumed all tokens as arr; try a heuristic:
            # If len(arr) >= 2, interpret the last element as k and rest as arr[:-1]
            if len(arr) >= 2:
                k = arr[-1]
                arr = arr[:-1]
        if k is None:
            # If k cannot be inferred, safest output is 0 (or raise).
            print(0)
            return
        ans = max_sum_window_k(arr, k)
        print(ans)
        return

    # Default fallback if MODE is mistyped
    # (Do not print debug text; just produce a neutral result)
    print(0)

if __name__ == "__main__":
    solve()