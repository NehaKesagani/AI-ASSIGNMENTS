from graph import graph_rep
from dijkstra import dijkstra

#to get shortest path 
def graphpath(previous, source, destination):

    path = []
    current = destination

    while current is not None:
        path.append(current)

        if current == source:
            break

        current = previous[current]

    path.reverse()

    if path[0] != source:
        return []

    return path

graph = graph_rep("indian_cities_dataset.csv")

print("\nAvailable Cities:")

for city in sorted(graph):
    print("-", city)
#inputs
source = input("\nEnter source city: ").strip()
destination = input("Enter destination city: ").strip()

if source not in graph:

    print(f"\nError: '{source}' is not in the dataset.")

elif destination not in graph:

    print(f"\nError: '{destination}' is not in the dataset.")

else:
#run dijkstra
    distances, previous = dijkstra(graph, source)

    path = graphpath(previous, source, destination) #shortest path 
#results
    print(f"\nSource      : {source}")
    print(f"Destination : {destination}")

    if not path:

        print("\nNo path exists between the source and destination cities.")

    else:

        print("\nShortest Path:")
        print(" → ".join(path))

        print(f"\nTotal Distance: {distances[destination]} km")