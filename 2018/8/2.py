def dfs(data):
    res = 0
    index = 2
    nodes, meta = data[:2]

    node_values = {}
    for n in range(nodes):
        val, read = dfs(data[index:])
        node_values.update({n+1 : val})
        index += read
    
    if nodes:
        res += sum(node_values[m] for m in data[index:index+meta] if m in node_values)
    else:
        res += sum(data[index:index+meta])
    
    return res, index+meta

data = list(map(int, input().split()))
print(dfs(data)[0])
