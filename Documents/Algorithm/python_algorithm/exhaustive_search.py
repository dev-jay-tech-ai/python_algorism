N = 11

ans = []
cnt = 0

def dfs(x):
    print(x)
    if x == 0: 
        return
    dfs(x//2) 
    ans.append(x%2)


dfs(N)
print(ans)