lst = input().split()
count = 0
print('решение 1')
for i in range(len(lst)):
    print(i + 1, lst[i][:10], end='\n')
print('решение 2')
for i in lst:
    count += 1
    print(count, i[:10], end='\n')
print('решение 3')
for i, j in enumerate(lst):
    print(i + 1, j[:10])
