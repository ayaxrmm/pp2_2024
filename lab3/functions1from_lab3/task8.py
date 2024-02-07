def spy_game(nums):
    b=[]
    c=[]
    for i in range(len(nums)):
        if nums[i]==0 or nums[i]==7:
            b.append(nums[i])
            c.append(nums[i])
    c=sorted(c)
    if b==c:
        return True
    return False
nums=[1,2,4,0,0,7,5]
print(spy_game(nums))
nums=[1,0,2,4,0,5,7]
print(spy_game(nums))
nums=[1,7,2,0,4,5,0]
print(spy_game(nums))