def total_sum(numbers):
    total = 0

    for index in range(len(numbers)):
        print('index = {}  number = {}'.format(index, numbers[index]))
        if isinstance(numbers[index], list):
            return total + total_sum(numbers[index])
        # print('index = {}  number = {}'.format(index, numbers[index]))
        total += numbers[index]
    return total    
