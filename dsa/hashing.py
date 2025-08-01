
# def two_sum(num:list[int],target:int):
#     dict1={}
#     n=len(num)
#     for i in range(n):
#         rem=target-num[i]
#         if rem in dict1:
#            return [dict1[rem],i]
#         dict1[num[i]]=i

# print(two_sum([5,1,8,2,6,4,9],12))  # Output: [1, 2] (1 + 9 = 10)


def two_sum(num:list[int],target:int):
    left=0
    right=len(num)-1
    while left<right:
        sum1=num[left]+num[right]
        if sum1==target:
            return [sum1,left+1,right+1]
        elif sum1>target:
           right-=1  
        else:
            left+=1

print(two_sum([5,10,15,16,23],26))  # Output: [1, 9] (1 + 9 = 10)

