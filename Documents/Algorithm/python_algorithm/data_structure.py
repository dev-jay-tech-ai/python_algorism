# -------------------------------
#       Data Structure
# -------------------------------

a, b = 'AbaAeCe', 'baeeACA'
hash = {}

for i in range(len(a)):
    hash[a[i]] = hash.get(a[i], 0) + 1
    hash[b[i]] = hash.get(b[i], 0) - 1
print(all(hash.values()))
print(hash.values())

# a, b = 'AbaAeCe', 'baeeACA'
# N = len(a)
# ans = 'YES'
# def hash (x):
#     hash = {}
#     for _x in x: hash[_x] = hash.get(_x, 0) + 1   
#     return hash

# hash_a, hash_b = hash(a), hash(b)
# for key, val in hash_a.items():
#     if not hash_b[key] == val:
#         ans = 'NO'
#         break
# print(ans)


# classes = 'CBA'
# N = 3
# plans = ['CBDAGE', 'FGCDAB', 'CTSBDEA']

# classes = 'AFC'
# N = 1
# plans = ['AFFDCCFF']

# for plan in plans:
#     ans = 'YES'
#     arr = list(classes)
#     for p in list(plan):
#         if not arr: break
#         if p == arr[0]:
#             arr.pop(0)

#     if arr: ans = 'NO'
#     print(ans)

# N,M = 5, 2
# patiences = [60, 50, 70, 80, 90]

# # N,M = 6, 0
# # patiences = [60, 60, 90, 60, 60, 60]
# target = patiences[M] # 70번 환자

# for _ in range(N):
#     p = patiences.pop(0)
#     if p < max(patiences):
#         patiences.append(p)
#     else: patiences.insert(0,p)

# print(patiences)

# ans = 0
# for i in range(N):
#     if patiences[i] == target:
#         ans = i
# print(ans)

# N,M = 8, 3
# prince = [ i+1 for i in range(N) ]
# cnt = 1

# while len(prince) > 1:
#     print(cnt)
#     if cnt == 3:
#         prince.pop(0)
#         cnt = 1
#     else:
#         prince.append(prince.pop(0))
#         cnt += 1
#     print(prince)

# print(prince[0])




# 3*(5+2)-9
# form = "3+5*2/(7-2)"
# arr = list(form)
# num = '123456789'
# ans = []
# stack = []
# for x in arr:
#     if x in list(num): 
#         ans.append(int(x))

#     else: 
#         stack.append(x)

 
# s = "( ) ( ( ( ( ) ( ) ) ( ( ) ) ( ) ) ) ( ( ) )"
# s = "( ( ( ( ) ( ( ) ( ) ) ) ( ( ) ) ( ) ) ) ( ( ) ( ) )"
# arr = s.split(' ')
# ans = []
# cnt = 0
# print(arr)
# for i, s in enumerate(arr):
#     if s == '(': ans.append('(')
#     else:  # s == ')'
#         ans.pop()
#         if arr[i-1] == '(': cnt += len(ans)
#         else: cnt += 1

# print(ans)
# print(cnt)



# arr = [5, 2, 7, 6, 8, 2, 3]
# ans = []
# # arr = [9, 9, 7, 7, 2, 5, 2, 6, 4, 1]
# cnt = 0
# ans.append(arr[0])
# while cnt < 3:
#     for i in range(1, len(arr)):
#         if ans[-1] >= arr[i]:
#             ans.append(arr[i])
#         elif ans[-1] < arr[i]: 
#             print(ans)
#             ans.pop()
#             ans.append(arr[i])
#             cnt += 1
# print(ans)


# cnt = 0
# lt, rt = 0, 1
# while cnt < 3:
#     print(arr[lt], arr[rt])
#     if arr[lt] > arr[rt]: 
#         print(arr.pop(rt))
#         cnt += 1
#     elif arr[lt] < arr[rt]: 
#         print(arr.pop(lt))
#         cnt += 1
#     else: # lt와 rt 가 같으면
#         print(arr[lt], arr[rt])
#         lt += 2
#         rt += 2

# print(arr)


