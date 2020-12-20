# this works only for when the arr is sorted
def all_binary_search(arr, x):
    N = len(arr)
    low = 0
    high = N - 1
    start_idx = -1
    while low <= high:
        mid = low + (high - low) // 2
        if x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        elif arr[mid] == x :
            high = mid - 1
            if mid == 0 or (x > arr[mid-1]):
                start_idx = mid
                break
    low = 0
    high = N - 1
    end_idx = -1
    while low <= high:
        mid = low + (high - low) // 2
        if x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        elif arr[mid] == x :
            low = mid + 1
            if mid == N-1 or (x < arr[mid+1]):
                end_idx = mid
                break

    if (start_idx != -1) & (end_idx != -1):
        return list(range(start_idx, end_idx+1))
    elif (start_idx == -1) & (end_idx != -1):
        return [start_idx]
    elif (start_idx != -1) & (end_idx == -1):
        return [end_idx]

    return []

def solution(nums, target):
    for i in range(len(nums)):
        other_half = target - nums[i]
        all_idx = all_binary_search(nums, other_half)
        try:
            if len(all_idx) >= 2:
                all_idx.remove(i)
            if len(all_idx) > 0:
                res = all_idx[0]
                if i < res:
                    return [i, res]
                else:
                    return [res, i]
        except Exception as e:
            pass


from collections import defaultdict
def solution(nums, target):
    vals = defaultdict(list)
    for i, v in enumerate(nums):
        vals[v].append(i)

    for i, v in enumerate(nums):
        other_half = target - v
        if vals.get(other_half) is not None:
            idx = vals.get(other_half)
            if (v == other_half) & (len(idx) == 1): # same node
                continue
            if len(idx) > 1:
                idx.remove(i)
            # print (i, idx)
            return [i, idx[0]]

