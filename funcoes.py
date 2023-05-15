from queue import Queue
import heapq



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
    'A': {'B': 3, 'C': 5,'D': 6, 'F': 8},
    'B': {'A': 3, 'C': 4, 'D': 6},
    'C': {'A': 2, 'B': 1, 'E': 10},
    'D': {'A': 7, 'B': 6, 'F': 8,'H': 7},
    'E': {'C': 10,'G': 4},
    'F': {'A': 8, 'D': 8, 'H': 8,'I': 8},
    'G': {'E': 5, 'I': 1, 'H': 3},
    'H': {'D': 2, 'F': 1, 'G': 1},
    "I" : {'F': 8,'G': 4}
    }


def dijkstra(graph, start, end):
    # Cria um dicionário para armazenar as distâncias dos nós ao nó inicial
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # A distância do nó inicial a ele mesmo é 0

    # Cria um dicionário para armazenar o caminho percorrido até cada nó
    path = {node: [] for node in graph}
    path[start] = [start]  # O caminho para o nó inicial é ele mesmo

    # Cria uma fila de prioridade para armazenar os nós visitados
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Ignora o nó se já tiver sido visitado com uma distância menor
        if current_distance > distances[current_node]:
            continue

        # Verifica os vizinhos do nó atual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Se encontrar um caminho mais curto para o vizinho, atualiza a distância e o caminho
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = path[current_node] + [neighbor]
                heapq.heappush(queue, (distance, neighbor))

    shortest_distance = distances[end]  # Menor distância para o nó final
    shortest_path = path[end]  # Caminho percorrido para o nó final

    return shortest_distance, shortest_path

start_node = 'A'
end_node = 'I'

shortest_distance, shortest_path = dijkstra(graphPeso, start_node, end_node)

print(f"A menor distância entre '{start_node}' e '{end_node}' é: {shortest_distance}")
print(f"O caminho percorrido é: {' -> '.join(shortest_path)}")
print(shortest_path)
