with open('data.txt') as file_content:
    data = file_content.read()


data = data.replace('   ', '\n')
data = data.split('\n')
data.pop()

l_list = []
r_list = []

for i, num in enumerate(data):
    if i % 2 == 0:
        l_list.append(int(num))
    else:
        r_list.append(int(num))

num_counter = {}

for num in r_list:
    try:
        num_counter[num] += 1
    except:
        num_counter[num] = 1

total = 0
for num in l_list:
    if num in num_counter:
        total += num*num_counter[num]


print(total)













# part 1
# l_list.sort()
# r_list.sort()
# total = 0

# for i in range(1000):
#     total += abs(l_list[i] - r_list[i])

# print(total)