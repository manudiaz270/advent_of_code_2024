with open('data.txt', 'r') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()
    for i, rep in enumerate(data):
        data[i] = rep.split(' ')
    for rep in data:
        for i, num in enumerate(rep):
            rep[i] = int(num)


def safe_report(report):
    if not (report == sorted(report) or report == sorted(report, reverse=True)):
        print(report, sorted(report, reverse=True))
        return False
    prev = ''
    for num in report:
        if not prev:
            prev = num
            continue
        if not (abs(int(num) - int(prev)) in [1,2,3]):
            return False
        
        prev = num
    return True




    
count = 0

for report in data:
    if safe_report(report):
        count += 1
        continue
    n_report = report[:]
    for i in range(len(report)):
        n_report.pop(i)
        if safe_report(n_report):
            count +=1
            break
        n_report = report[:]


print(count)




















# counter = 0
# for report in data:
#     status = 0
#     prev = ''
#     for num in report:
#         if not prev:
#             prev = num
#             continue

#         if not status:
#             if int(num) - int(prev) >
            

