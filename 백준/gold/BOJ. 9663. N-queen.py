import sys
N = int(sys.stdin.readline().rstrip())
rows = [0] * N #row[i] = j 라면 i행 j열에 퀸이 있다는 소리
ans = 0

def is_safe(row):
    # 같은 행 같은 열 같은 대각선에 체스가 있는지 체크
    for i in range(row): # row인 이유 => 이전에 배치된 퀸들과의 충돌 확인 역할
        if rows[i] == rows[row] or abs(row - i) == abs(rows[row] - rows[i]):
            return False

    return True


def back_tracking(row):
    global ans
    if row == N:
        ans += 1

    else:
        for col in range(N):
            rows[row] = col
            if is_safe(row):
                back_tracking(row + 1)


back_tracking(0)
print(ans)