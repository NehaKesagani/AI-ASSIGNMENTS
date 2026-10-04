import heapq

def dijkstra(graph, source):

    distances = {}
    previous = {}

    #intialize distances and previous
    for city in graph:
        distances[city] = float("inf")
        previous[city] = None

    distances[source] = 0

    #priority queue (distance, city)
    pq = [(0, source)]

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        if current_distance > distances[current_city]: #ignore outdated entry
            continue
        for neighbor, road_distance in graph[current_city]: #neighnour cities

            new_distance = current_distance + road_distance

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_city

                heapq.heappush(
                    pq,
                    (new_distance, neighbor)
                )

    return distances, previous