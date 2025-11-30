# Binary Search
N = 32
arr = [23, 87, 65, 12, 57, 32, 99, 81]
lt, rt = 0, len(arr)-1
arr.sort()
print(arr)
ans = 0
while(lt <= rt):
    mid = (lt + rt) // 2
    # print(lt, rt, mid)
    if arr[mid] == N:
        ans = mid+1 # mid는 인덱스, 순서는 +1 
        break
    elif arr[mid] < N:
        print(lt, rt, arr[mid], 'A')
        lt = mid + 1 # 확인한 mid 보다 작으므로 -1
    else: # arr[mid] > N:
        print(lt, rt, arr[mid], 'B')
        rt = mid -1  # 확인한 mid 보다 크므로 +1

print(ans)

