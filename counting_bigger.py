input_list = [int(i) for i in input().split()]
count = 0
for i in range(len(input_list)-1):
    if input_list[i] < input_list[i + 1]:
        count += 1
print(count)
