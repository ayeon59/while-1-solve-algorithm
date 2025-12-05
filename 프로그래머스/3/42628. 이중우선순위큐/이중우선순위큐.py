import heapq

def solution(operations):
    min_h = []  # (값, id)
    max_h = []  # (-값, id)  -> 최대힙처럼 사용
    visited = [False] * len(operations)  # 각 연산별로 "살아있는지" 표시

    for i, op in enumerate(operations):
        cmd, num_str = op.split()
        num = int(num_str)

        if cmd == "I":  # 삽입
            heapq.heappush(min_h, (num, i))
            heapq.heappush(max_h, (-num, i))
            visited[i] = True

        else:  # "D" 삭제
            if num == 1:  # 최대값 삭제
                # 이미 삭제된 애들은 버리기
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    _, idx = heapq.heappop(max_h)
                    visited[idx] = False
            else:  # 최소값 삭제 (num == -1)
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    _, idx = heapq.heappop(min_h)
                    visited[idx] = False

    # 최종 정리: 양쪽 힙에서 이미 죽은 애들 제거
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)

    # 큐가 비었으면 [0, 0]
    if not min_h or not max_h:
        return [0, 0]

    # 최대값, 최소값 반환
    max_val = -max_h[0][0]
    min_val = min_h[0][0]
    return [max_val, min_val]
