import sys
#sys.stdin = open('LIBRARY.txt','r')
#input = sys.stdin.readline

def dfs_lien_thong(u,visited,graph,V,ans):
    visited[u] = True 
    ans = min(ans,V[u])
    for v in graph[u]:
        if not visited[v]:
            ans = dfs_lien_thong(v,visited,graph,V,ans)
    return ans



n,m = map(int,sys.stdin.readline().split())
V = [0] + list(map(int,sys.stdin.readline().split()))
graph =[[] for i in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
visited =[False]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        ans += dfs_lien_thong(i,visited,graph,V,float('inf'))
print(ans)







'''

Test case #1:	AC	[0,023s,	10,88 MB]	(1/1)
Test case #2:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #3:	AC	[0,022s,	11,38 MB]	(1/1)
Test case #4:	AC	[0,022s,	11,25 MB]	(1/1)
Test case #5:	AC	[0,022s,	11,38 MB]	(1/1)
Test case #6:	IR  (RecursionError)	[0,101s,	27,87 MB]	(0/1)
Test case #7:	IR  (RecursionError)	[0,118s,	25,25 MB]	(0/1)
Test case #8:	IR  (RecursionError)	[0,148s,	31,45 MB]	(0/1)
Test case #9:	IR  (RecursionError)	[0,146s,	31,74 MB]	(0/1)
Test case #10:	IR  (RecursionError)	[0,148s,	31,75 MB]	(0/1)
'''




















