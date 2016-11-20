import smart_backend

test = smart_backend
graph = test.Graph()
root = graph.root
print(root.string())
print(graph.height)
node1 = test.Node("level 2")
graph.connect_to(root, node1)
print(root.height)
node2= test.Node("level 3")
graph.connect_to(node1, node2)
node3= test.Node("level 4")
graph.connect_to(node2, node3)
print(root.get_height())
graph.disconnect_from(node2,node3)
print(graph.get_height())
graph.disconnect_from(node1,node2)
print(graph.get_height())
graph.disconnect_from(root, node1)
print(graph.get_height())