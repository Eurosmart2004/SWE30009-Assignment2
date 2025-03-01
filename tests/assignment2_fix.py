def split_and_sort(nums):

    # check input list length 
    if len(nums) > 30:
        return "Error: Input list should contain less number integers."

    # filter numbers into two separate lists
    pos_nums = [num for num in nums if num > 0]
    neg_nums = [num for num in nums if num <= 0]

    # sort
    neg_nums = sorted(set(neg_nums))
    pos_nums = sorted(set(pos_nums))

    print("Positive numbers:", pos_nums)
    print("Negative numbers:", neg_nums)

    return neg_nums, pos_nums

