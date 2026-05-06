# 1
file = open('17-338.txt')
m = []
for line in file:
    ch = int(line)
    m.append(ch)

# 2
m_min = min(m)

# 3
c = 0
max_sum = -1000000000
for i in range(len(m) - 1):
    if m[i] % 117 == m_min or m[i+1] % 117 == m_min:
        c += 1
        max_sum = max( m[i]+m[i+1] , max_sum )
        
print(c, max_sum)