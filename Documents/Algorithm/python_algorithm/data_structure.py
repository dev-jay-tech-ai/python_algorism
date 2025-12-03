# -------------------------------
#       Data Structure
# -------------------------------


N = 5
arr = [2, 4, 5, 1, 3]
arr = [3, 2, 10, 1, 5, 4, 7, 8, 9, 6]
ans = []
res = []
last = 0

for i in range((N//2)+1): # 2번 돈다
    if len(arr) == 1 and last < arr[-1]:
        ans.append(arr.pop())
        res.append('R')
        print('중간확인: ',ans)
        break
    if last < arr[0]: 
        ans.append(arr.pop(0))
        res.append('L')
        last = ans[-1]
    if last < arr[-1]: 
        ans.append(arr.pop())
        res.append('R')
        last = ans[-1]

    

print(ans)
print(res)