def dfs(depth):
    global result
    if depth == int(change):
        result = max(int(''.join(nums)), result)
        return

    for i in range(len(nums)):
        # min_num = nums[i]
        for j in range(i+1, len(nums)):
            # max_num = nums[j]
            # if max_num >= min_num:
            nums[i], nums[j] = nums[j], nums[i]
            if [''.join(nums), depth] not in ans:
                ans.append([''.join(nums), depth])
                dfs(depth+1)
            nums[i], nums[j] = nums[j], nums[i]

T = int(input())
for tc in range(1, T+1):
    num, change = input().split()
    result = 0
    nums = list(num)
    ans = []
    dfs(0)

    print(f'#{tc} {result}')
