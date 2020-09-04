def has_negatives(nums):
    """
    YOUR CODE HERE
    """
    num_dict = {}
    res = []
    for n in nums:
        if num_dict.get(abs(n)):
            res.append(abs(n))
        else:
            num_dict[abs(n)] = n
    return res


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
