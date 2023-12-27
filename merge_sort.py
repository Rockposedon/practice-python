# def merge_sort(arr):
#     if len(arr) > 1:
        
    
#         mid  = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#         merge_sort(left)
#         merge_sort(right)

#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j] :
#                 arr[k] = left[i]
#                 i += 1
#             else :
#                 arr[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             arr[k] =left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1
#     print(arr)
# arr = [2,3,1,6,8,9,4,10,-1,-2,100]
# merge_sort(arr)

def searchRange( nums, target) :
    for i in range(0,len(nums)) :
        # print(i)
        if i == target:
            start = (nums.index(target))
    for j in range(0,len(rev_nums)):
        if j == target:
            last = (nums.index(target))
        # else :
        #     print(-1,-1)
    print(start,last)
        

    
            # if target in nums:
            #     print(nums.index(target))
        # else :
            # print(-1,-1)
nums = [1,2,3,4,4,5,6,14]
rev_nums = nums[::-1]
target = 4
searchRange(nums,target)


            
