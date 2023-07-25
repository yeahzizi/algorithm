def solution(nums):
    pokemon = {}
    answer = 0

    for i in nums:
        pokemon[i] = 1

    if len(nums) / 2 >= len(pokemon):
        answer = len(pokemon)
    if len(nums) / 2 < len(pokemon):
        answer = len(nums) / 2

    return answer