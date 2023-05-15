from queue import Queue


graph = {
      "A" : ["B","C","D","F"],
      "B" : ["A","C","D"],
      "C" : ["A","B","E"],
      "D" : ["A","B","F","H"],
      "E" : ["C","G"],
      "F" : ["A","D","H","I"],
      "G" : ["E","I","H"],
      "H" : ["D","F","G"],
      "I" : ["F","G"]
 }
#
#visited = []
#queue = []

#def bfs(visited, graph, node):
 #   visited.append(node)
  #  queue.append(node)

   # while queue:
    #    m = queue.pop(0)
     #   print(m,end = " ")

      #  for neighbour in graph[m]:
       #     if neighbour not in visited:
        #        visited.append(neighbour)
         #       queue.append(neighbour)


def bfs(graph, inicial, final):
    visited = {}
    level = {}
    parent = {}
    bfs_transversal_output = []
    queue = Queue()

    for no in graph.keys():
        visited[no] = False
        parent[no] = None
        level[no] = -1
    s = inicial
    visited[s] = True
    level[s] = 0
    queue.put(s)

    while not queue.empty():
        u = queue.get()
        bfs_transversal_output.append(u)

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u]+1
                queue.put(v)
    print("bfs",bfs_transversal_output)

    f = final
    path = []
    while f is not None:
        path.append(f)
        f = parent[f]
    path.reverse()
    print('menor caminho',path)
    return path

graphPeso = {
    'A': {'B': 5, 'C': 2,'D': 1, 'F': 1},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'E': 1},
    'D': {'A': 3, 'B': 1, 'F': 4,'H': 5},
    'E': {'C': 4,'G': 4},
    'F': {'A': 3, 'D': 1, 'H': 4,'I': 5},
    'G': {'E': 5, 'I': 1, 'H': 3},
    'H': {'A': 2, 'B': 1, 'D': 1},
    "I" : {'C': 4,'G': 4}
    }



