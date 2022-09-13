number = int(input(f'Type a range of numbers and i will get the narcisist ones: '))

for i in range(number):
    num = 0
    for j in str(i):
        num += int(j)**len(str(i))
    if num == i:
        print(num)  
