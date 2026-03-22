def remove_duplicates(lst):
    result=[]
    for i in lst:
        if i  not in result:
            result.append(i)
    return result
print(remove_duplicates([1,2,3,4,5,6,7,7,7,7,1,2,3,3]))
