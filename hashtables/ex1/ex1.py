def get_indices_of_item_weights(weights, length, limit):
    
    memo = {}
    print(weights, length, limit)

    for lnth in range(length):
        wght = weights[lnth]
        print(f'\nWEIGHTS VAR:{weights[lnth]}')
        indi = limit - wght
        print(f'\nINDI VAR:{indi}')
        if indi in memo:
            x = memo[indi]
            print(f'\n X VAR:{x}')
            print('\n')
            print(memo)
            return [lnth, x]
        else:
            memo[wght] = lnth

    return None


# Given a package with a weight limit `limit` and a list `weights` of item
# weights, implement a function `get_indices_of_item_weights` that finds
# two items whose sum of weights equals the weight limit `limit`. Your
# function will return a tuple of integers that has the following form:

# ```
# (zero, one)
# ```

# where each element represents the item weights of the two packages.
# _**The higher valued index should be placed in the `zeroth` index and
# the smaller index should be placed in the `first` index.**_ If such a
# pair doesn’t exist for the given inputs, your function should return
# `None`.