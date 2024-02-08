def common_elements(list1, list2):
    new=[]
    for i in list1:
        for j in list2:
            if i==j:
                new.append(i)
            else:
                continue
    return new
list1=[1,2,3,4,5,6]
list2=[1,3,5,7,9,11]
print(common_elements(list1,list2))
