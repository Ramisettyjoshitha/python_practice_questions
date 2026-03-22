def expense(expense):
    total=0
    for num in expense:
        total+=num
    average=total/len(expense)
    return total,average
data=[100,200,300,400]
result=expense(data)
print("total:",result[0])
print("average:",result[1])