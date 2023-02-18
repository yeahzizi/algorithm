N = int(input())
cnt = 0
m_list = []

for _ in range(N):
    money = int(input())
    if money == 0:
        m_list.pop(-1)
    else:
        m_list.append(money)

print(sum(m_list))