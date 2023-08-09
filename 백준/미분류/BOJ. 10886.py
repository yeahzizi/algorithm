N = int(input())
cute = 0
for i in range(N):
    vote = int(input())
    if vote == 1:
        cute += 1
        continue
    elif vote == 0:
        cute -= 1
        continue

if cute > 0:
    print("Junhee is cute!")
elif cute < 0:
    print("Junhee is not cute!")


