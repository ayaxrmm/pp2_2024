def unique(list):
    unique_list=[]
    for i in list:
        is_unique=True
        for j in unique_list:
            if i==j:
                is_unique=False
                break
        if is_unique:
            unique_list.append(i)
    return unique_list

list=[1, 3, 2, 1, 3, 5]
print(unique(list))
