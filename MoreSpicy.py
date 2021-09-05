import os
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while True :
        min_ = heapq.heappop(scoville)
        if min_ >= K :
            break
        elif len(scoville) == 0 :
            return -1 
        second_min = heapq.heappop(scoville)
        heapq.heappush(scoville, min_ + (second_min * 2))
        cnt += 1
    return cnt

os.system('cls')
print("정답 : ",solution([1,2,3],11))
print("정답 : ",solution([1, 2, 3, 9, 10, 12],7))
print("정답 : ",solution([12, 10, 9, 3, 2, 1],7))