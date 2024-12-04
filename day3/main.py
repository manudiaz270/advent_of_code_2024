import re
with open('data.txt', 'r') as f:
    data = f.read()



parsed_str = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)


def find_mul(mul):
    n_mul = mul[4:-1]
    n_mul = n_mul.split(',')
    return int(n_mul[0])*int(n_mul[1])

total = 0
enabled = True
for func in parsed_str:
    if func[0] == 'm' and enabled:
        total += find_mul(func)
    if func[0] == 'd':
        if len(func) == 4:
            enabled = True
        else:
            enabled = False


print(total)