import smart_backend

test = smart_backend
node = test.Node("example 1")
print(node.string())
graph = test.Graph()
d = graph.get()
print(d.pop().string())