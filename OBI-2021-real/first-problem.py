
x = int(input())
n = int(input())
m = 0

for mes in range(1,n+1):
    m = m + x - int(input())
    if m < 0:
        m = 0

print(m+x)