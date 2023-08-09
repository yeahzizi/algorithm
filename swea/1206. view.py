for test_case in range(1, 11):
    house = int(input())
    house_list = list(map(int, input().split()))
    view_building = 0
    s = 2 #왼쪽과 오른쪽 두 칸에는 건물이 없으므로 s를 이용해 제외함

    for h in range(s, house - s): #건물이 있는 부분만 for문 적용
        view = house_list[h - s] #건물이 있는 칸은 view에 넣기
        for v in range(h - s + 1, h + s + 1): #양쪽 2개 칸 비교
            if h == v: #자신은 빼고 최대값 찾기
                continue
            elif view < house_list[v]: #최댓값이 나올때마다 view가 변경된다
                view = house_list[v]
        if house_list[h] > view: #인덱스 h의 건물이 view보다 높으면 조건에 맞는 건물이므로,
            view_building += house_list[h] - view #h건물 높이에서 view를 뺀 값을 view_building에 계속 더한다.
            
    print(f'#{test_case} {view_building}')