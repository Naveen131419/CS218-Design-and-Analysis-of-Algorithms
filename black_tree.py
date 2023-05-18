n, m = map(int, input().split())

adj_list = [[] for _ in range(n)]
for i in range(1, n):
    parent = int(input())
    adj_list[parent].append(i)

traitors = set()
for i in range(m):
    traitor = int(input())
    traitors.add(traitor)
    adj_list[traitor] = []

def dfs(node):
    size = 1
    for child in adj_list[node]:
        if child in traitors:
            continue
        size += dfs(child)
    return size

max_size = 0
for i in range(n):
    if i in traitors:
        continue
    size = dfs(i)
    max_size = max(max_size, size)

print(max_size)
