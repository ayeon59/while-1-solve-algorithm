import heapq

def solution(n, works):
    # 야근시간보다 일이 적으면 걍 0
    if sum(works) <= n:
        return 0

    # 파이썬 heapq는 최소힙이라, 음수로 바꿔서 최대힙처럼 사용
    h = [-w for w in works]
    heapq.heapify(h)

    for _ in range(n):
        largest = heapq.heappop(h)  # 가장 큰 값(= 가장 작은 음수)

        # 0이면 더 이상 줄일 일이 없음 (다 0이라는 뜻)
        if largest == 0:
            heapq.heappush(h, largest)
            break

        # 1 줄이기: 음수니까 +1을 해주면 절댓값이 1 줄어듦
        largest += 1
        heapq.heappush(h, largest)

    # 제곱합 계산 (음수든 양수든 제곱하면 같으니까 그냥 v*v)
    return sum(v * v for v in h)
