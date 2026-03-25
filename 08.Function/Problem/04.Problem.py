#Find largest number in a list

def find_max(numbers):
    max_num = numbers[0]
    
    for num in numbers:
        if num > max_num:
            max_num = num
            
    return max_num

nums = [3, 7, 2, 9, 5]
print(find_max(nums))
