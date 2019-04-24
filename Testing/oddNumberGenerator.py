def get_odd_numbers(a):
    odd_numbers = []
    for i in range(1, a + 1):
        if i % 2 == 1:
            odd_numbers.append(i)
    return odd_numbers
