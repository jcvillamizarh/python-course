def multiply_numbers(numbers):
    new_list = list(map(lambda number: number * 2, numbers))
    return new_list

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)