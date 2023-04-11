def dfs(data):
    res = 0
    index = 2
    nodes, meta = data[:2]
    for _ in range(nodes):
        val, read = dfs(data[index:])
        res += val
        index += read
    
    res += sum(data[index:index+meta])
    return res, index+meta

data = list(map(int, input().split()))

print(dfs(data)[0])
