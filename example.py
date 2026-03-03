matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

result = [row[0] for row in matrix]

#print(result)


data = [10,20,30,40,50]

data4 = data[::-1]
data1 = data.reverse()
data2 = sorted(data,reverse=True)
data3 = data.sort(reverse=True);data.reverse()

print(data4)
print(data1)
print(data2)
print(data3)

