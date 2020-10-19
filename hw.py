data = []
odd = []
even = []
up50 = []
dw50 = []
with open('d:\\1\\test.txt', 'r') as item:
    for line in item:
        data.append(line.strip())
data = list(map(int, data))
print('讀取出的數據為:', data)
data.sort()
print('排列後出來的數列為:', data)
for num in data:
    if (num % 2) == 0:
        even.append(num)
    elif (num % 2) != 0:
        odd.append(num)
print('奇數為:', odd)
print('偶數為:', even)
for num1 in data:
    if num1 <= 50:
        dw50.append(num1)
    else:
        up50.append(num1)
print('小於50的數有:', dw50)
print('大於50的數有:', up50)




