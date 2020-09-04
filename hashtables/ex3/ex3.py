def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dictionary = {}

    for index in arrays:
        for arr in index:
            if arr in dictionary:
                dictionary[arr] += 1
            else:
                dictionary[arr] = 1

    res = [arr[0] for arr in dictionary.items() if arr[1] == len(arrays)]

    return res

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(20, 30)) + [1, 2, 3])
    arrays.append(list(range(30, 40)) + [1, 2, 3])

    print(intersection(arrays))
