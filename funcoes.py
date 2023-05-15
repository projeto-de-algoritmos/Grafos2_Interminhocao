from queue import Queue
import heapq

"""

graph = {
      "A" : ["B","C","D","F"],
      "B" : ["A","C","D"],
      "C" : ["A","B","E"],
      "D" : ["A","B","F","H"],
      "E" : ["C","G"],
      "F" : ["A","D","H",'ICC NORTE'],
      "G" : ["E",'ICC NORTE',"H"],
      "H" : ["D","F","G"],
      'ICC NORTE' : ["F","G"]
 }


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
"""

graphPeso = { 
    'ICC SUL': {'IB': 3, 'IDA': 5,'REITORIA': 6, 'CEUBINHO': 8},
    'IB': {'ICC SUL': 3, 'IDA': 2, 'REITORIA': 6},
    'IDA': {'ICC SUL': 2, 'IB': 2, 'FT': 10},
    'REITORIA': {'ICC SUL': 7, 'IB': 6, 'CEUBINHO': 8,'BCE': 7},
    'FT': {'IDA': 10,'FD': 4},
    'CEUBINHO': {'ICC SUL': 8, 'REITORIA': 8, 'BCE': 8,'ICC NORTE': 8},
    'FD': {'FT': 5, 'ICC NORTE': 2, 'BCE': 3},
    'BCE': {'REITORIA': 2, 'CEUBINHO': 1, 'FD': 1},
    'ICC NORTE' : {'CEUBINHO': 8,'FD': 2}
    }


def dijkstra(graph, start, end):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0


    path = {node: [] for node in graph}
    path[start] = [start]

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Ignora o nó se já tiver sido visitado com uma distância menor
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight


            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = path[current_node] + [neighbor]
                heapq.heappush(queue, (distance, neighbor))

    shortest_distance = distances[end]
    shortest_path = path[end]

    print(f"A menor distância entre '{start}' e '{end}' é: {shortest_distance}")
    print(f"O caminho percorrido é: {' -> '.join(shortest_path)}")
    print(shortest_path)


    return shortest_distance, shortest_path
