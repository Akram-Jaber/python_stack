
def countdown(x):
    for i in range(x+1,1,-1):
        x=x-1
        print(x)
print(countdown(5))

def print_and_return(numbers):
    print(numbers[0])
    return numbers[1]
result = print_and_return([1, 2])
print("Returned value:", result)

def first_plus_length(lst):
    return lst[0] + len(lst)
result = first_plus_length([1, 2, 3, 4, 5])
print("Result:", result)

def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    new_list = [x for x in lst if x > lst[1]]
    print(len(new_list))
    return new_list
result = values_greater_than_second([5, 2, 3, 2, 9, 4])
print("Result:", result)
result = values_greater_than_second([3])
print("Result:", result)

def length_and_value(size, value):
    return [value] * size
result = length_and_value(4, 7)
print("Result:", result)
result = length_and_value(6, 2)
print("Result:", result)

