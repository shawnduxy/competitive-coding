n = int(input())

a = []
for _ in range(n):
    a.append(int(input()))

a.sort(reverse=True)

gold = 0
silver = 0
bronze = 0
count = 0

for i in a:
    if i == gold or i == silver:
        pass
    elif i == bronze:
        count = count + 1
    elif gold == 0:
        gold = i
    elif silver == 0:
        silver = i
    elif bronze == 0:
        bronze = i
        count = count + 1
    else:
        break

print(bronze, count)
