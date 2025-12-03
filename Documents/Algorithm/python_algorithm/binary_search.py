# --------------------
# Greedy : greedy is sorting
# --------------------
N = 8
r_sque = [5, 3, 4, 0, 2, 1, 1, 0]
#_sque = [1, 2, 3, 4, 5, 6, 7, 8]
arr = [0] * N

for i in range(N):
    idx = r_sque[i]
    if arr[idx] == 0: # 비었다면
        arr[r_sque[i]] = i+1
    else: # 이미 숫자가 있다면
        cnt = 
        for j in range(N):
            if arr[j] == 0:
                cnt += 1
            if cnt == idx:
                arr[j] = arr[j]
                cnt = 0

print(arr)

# -------------------------------
#       Data Structure
# -------------------------------


N = 5
arr = [2, 4, 5, 1, 3]
arr = [3, 2, 10, 1, 5, 4, 7, 8, 9, 6]
ans = []
res = []
last = 0

# for i in range((N//2)+1): # 2번 돈다
#     if len(arr) == 1 and last < arr[-1]:
#         ans.append(arr.pop())
#         res.append('R')
#         print('중간확인: ',ans)
#         break
#     if last < arr[0]: 
#         ans.append(arr.pop(0))
#         res.append('L')
#         last = ans[-1]
#     if last < arr[-1]: 
#         ans.append(arr.pop())
#         res.append('R')
#         last = ans[-1]

    

# print(ans)
# print(res)


# arr = [2,4,5,1,3]
# sequence = []

# while arr:
#     if len(arr) == 1 and arr[-1] > sequence[-1]:
#         sequence.append(arr.pop())
#     else: arr.pop()
#     if sequence: 
#         if arr[0] < arr[-1] and arr[0] > sequence[-1]:
#             sequence.append(arr.pop(0))
#         elif arr[0] > arr[-1] and arr[-1] > sequence[-1]:
#             sequence.append(arr.pop())
#         else: arr.pop()
#     else:
#         if arr[0] < arr[-1]: sequence.append(arr.pop(0))
#         else: sequence.append(arr.pop())
#     print(sequence)   
# print(sequence)

# N,M = 5, 140 # 구명 보트에 탈 수 있는 제한 몸무게
# weights = [90, 50, 70, 100, 60]
# weights.sort()
# print(weights)

# ans = 0

# while weights: # 배열이 비어있지 않으면
#     if len(weights) == 1:   # 마지막에 베열에 1개의 숫자가 남으면 arr[0]과 arr[-1] 은 같은 숫가 된다 같은 수를 2번 더하면 논리적 오류가 발생한다
#         ans += 1            # 그래서 다음과 같은 별도의 처리가 필요하다
#         break
#     if weights[0] + weights[-1] <= M: 
#         weights.pop(0)
#         weights.pop()
#     else: 
#         weights.pop()
#     ans += 1
#     print(weights)
# print(ans)


# N, M= 10, 50 # 높이 조정 횟수
# boxes = [ 69, 42, 68, 76, 40, 87, 14, 65, 76, 81 ]
# boxes.sort()

# for _ in range(M):
#     boxes[-1] -= 1
#     boxes[0] += 1
#     boxes.sort()

# print(boxes[-1]-boxes[0])

# N = 5
# arr = [[172, 67],[183, 65],[180, 70],[170, 72],[181, 60]]
# arr.sort(key=lambda x: -x[0])
# ans = 0
# print(arr)
# max_w = 0
# for _, w in arr:
#     if w >= max_w: # 자기보다 키 큰 사람보다 몸무게는 큼(합격)
#         max_w = w # 몸무게 갱신
#         ans += 1
# print(ans)

# 이중 for 문은 효율적이지 못하다 함
# ans = 0 
# for i in range(N):
#     for j in range(i+1, N):
#         print(arr[i][1], arr[j][1])
#         if arr[i][1] < arr[j][1]: # 키는 내가 더 작음, 몸무게만 비교하면 됨!
#             break
#     else: ans += 1


# --------------------
# Binary Search
# --------------------

# Coordinate

# N,M = 5, 3
# coord = [1,2,8,4,9]
# coord.sort()
# lt, rt = min(coord), max(coord)
# ans = 0

# def Check(distance):
#     prev = 0 # 첫 번째 말을 배치
#     for h in range(1, M):
#         ccoord[prev + 1]

#     return

# while lt <= rt:
#     mid = (lt+rt)//2 # 두 말사이의 최대 거리
#     if Check() < M: # 모든 말을 포용하지 못하면
#         rt = mid - 1 # 두 말사이의 최대거리를 줄인다.
#     else:
#         lt = mid + 1 # 두 말 사이의 최대거리를 늘인다.

# N, M = 9, 3 # CD 개수
# song_t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# start, end = 1, sum(song_t) 
# max_cap = max(song_t) 
# ans = 0
# def Count(capacity):
#     tmp, cnt = 0, 1

#     for t in song_t:
#         print(tmp, t, cnt)
#         if tmp+t > capacity: # 노래를 한번 넣어보는 기분으로 ..
#             cnt += 1
#             tmp = t
#         else: # 같거나 작으면
#             tmp += t
#     return cnt

# while start <= end:
#     mid = (start+end)//2 # 최대 시간
#     # 각 cd에 몇개 담을 수 있는지
#     print('mid: ', mid)

#     times = Count(mid)
      
#     print('cnt: ', times)
#     if mid >= max_cap and times <= M: # CD 개수 확인
#         ans = mid
#         end = mid - 1  
#     else: 
#         start = mid +1
# print(ans)

# N=4
# M=11 # 필요한 랜선의 개수
# arr = [ 802, 743, 457, 539 ]

# start = 0 
# end = min(arr)//(M//N)
# ans = 0

# while start <= end: 
#     mid = (start+end)//2 # 랜선의 길이
#     tmp = sum([ a//mid for a in arr ])
#     print(mid)
#     if tmp >= M: 
#         ans = mid
#         start = mid + 1
#     else: end = mid - 1

# print(ans)


# N = 32
# arr = [23, 87, 65, 12, 57, 32, 99, 81]
# lt, rt = 0, len(arr)-1
# arr.sort()
# print(arr)
# ans = 0
# while(lt <= rt):
#     mid = (lt + rt) // 2
#     # print(lt, rt, mid)
#     if arr[mid] == N:
#         ans = mid+1 # mid는 인덱스, 순서는 +1 
#         break
#     elif arr[mid] < N:
#         print(lt, rt, arr[mid], 'A')
#         lt = mid + 1 # 확인한 mid 보다 작으므로 -1
#     else: # arr[mid] > N:
#         print(lt, rt, arr[mid], 'B')
#         rt = mid -1  # 확인한 mid 보다 크므로 +1

# print(ans)

