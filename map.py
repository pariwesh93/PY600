nums=[8, 2, 1, 3, 5, 6]
sq=[]
index=0
while index<len(nums):
    item=nums[index]
    sq.append(item**2)
    index=index+1
print(sq)