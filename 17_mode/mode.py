def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    max_num = max(freq.values())

    for (num, occ) in freq.items():
        if occ == max_num:
            return num