nums = [5,7,7,8,8,10]
target = 8

def findFirst(nums, target):
    left, right = 0, len(nums) - 1
    first_pos = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            first_pos = mid
            right = mid - 1  
            
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return first_pos

def findLast(nums, target):
    left, right = 0, len(nums) - 1
    last_pos = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            last_pos = mid
            left = mid + 1  
            
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return last_pos

def searchRange(nums, target):
    return [findFirst(nums, target), findLast(nums, target)]

print(searchRange(nums, target))
