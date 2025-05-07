MAX_DEPTH = 1000


def debug_print(*args, **kwargs):
    # print(*args, **kwargs)
    pass


# find the first index of a value greater than val
def find_first_index_gt_val(arr, val):
    i = 0
    low = 0
    high = len(arr) - 1
    while low < high and i < MAX_DEPTH:
        mid = (high + low) // 2
        debug_print([" - ", i, [low, high], "mid:", mid, "val:", val, arr])
        # move the low pointer to the right if arr[mid] <= val
        # ...so that we can get the largest smaller value
        if arr[mid] <= val:
            low = mid + 1
        else:
            high = mid
        i += 1
    # low should now have the smallest value > val
    debug_print(["FINAL:", [low, high], "low:", low, "val:", val, arr])
    return low


# find the largest index for the value less than val
def find_last_index_lt_val(arr, val):
    i = 0
    low = 0
    high = len(arr) - 1
    while low < high and high - low > 1 and i < MAX_DEPTH:
        mid = (high + low) // 2
        debug_print([" - ", i, [low, high], "mid:", mid, "val:", val, arr])
        if arr[mid] < val:
            low = mid
        else:
            high = mid
        i += 1
    debug_print(["FINAL:", [low, high], "low:", low, "val:", val, arr])
    return low


def find_first_index_of_exact_match(arr, val):
    pass
    low = 0
    high = len(arr) - 1
    i = 0
    # continue conditions:
    # - low < high (if low == high we are done)
    # - high and low are not adjacent
    # - too many iterations
    while low < high and high - low > 1 and i < MAX_DEPTH:
        mid = (high + low) // 2
        debug_print([" - ", i, [low, high], "mid:", mid, "val:", val, arr])
        i += 1
        if arr[mid] < val:
            low = mid + 1
        else:
            high = mid
    debug_print(["FINAL:", [low, high], "low:", low, "val:", val, arr])
    if arr[low] == val:
        return low
    elif arr[high] == val:
        return high
    else:
        return None
