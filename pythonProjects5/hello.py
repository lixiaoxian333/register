def deduplication(self, nums):#找出排序数组的索引
    for i in range(len(nums)):
        if nums[i]==self:
            return i
    i=0
    for x in nums:
        if self>x:
            i+=1
    return i
print(deduplication(5, [1,3,5,6]))