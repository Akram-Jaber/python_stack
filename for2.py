def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
my_list = [-1, 0, 5, 7]
biggie_size(my_list)
print(my_list)

def count_positives(list):
    count = 0
    for i in list:
        if i > 0:
            count += 1
    list[-1] = count
    return list
my_list1 = [-1,0,1,1]
count_positives(my_list1)
print(my_list1)


def sum(list):
    count=0
    for i in list:
        count=i+count
    return count
my_list=[1,2,3,9]
print(sum(my_list))


def sum(list):
    count=0
    for i in list:
        count=i+count
    avg=count/len(list)
    return avg
my_list=[1,2,3,2]
print(sum(my_list))


def find_range(list):
    for i in range(len(list)):
        return len(list)
my_list=[1,2,3,2,7,7]
print(find_range(my_list))

def find_min(list):
    min=list[0]
    for i in list:
        if(min>i):
            min=i
    return min    
my_list=[0,2,4,3,-1,9]
print(find_min(my_list))

def find_max(list):
    min=list[0]
    for i in list:
        if(min<i):
            min=i
    return min    
        
my_list=[0,10,4,3,-1,9]
print(find_max(my_list))


def ultimate_analysis(list):
    if not list:
        return None
    
    analysis = {
        'sumTotal': sum(list),
        'average': sum(list) / len(list),
        'minimum': min(list),
        'maximum': max(list),
        'length': len(list)
    }
    return analysis
result = ultimate_analysis([37, 2, 1, -9])
print(result)

def reverse_list(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
    return lst
result = reverse_list([9, 2, 5,6,-3])
print(result)



