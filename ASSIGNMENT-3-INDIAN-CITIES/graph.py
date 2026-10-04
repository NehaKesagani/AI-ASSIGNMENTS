import pandas as pd


def graph_rep(filename):
    #load datsset
    df = pd.read_csv(filename)

    graph = {}

    for _, row in df.iterrows():

        source = row["Source"]
        destination = row["Destination"]
        distance = row["Distance(km)"]

        if source not in graph: #add source if not present
            graph[source] = []

        if destination not in graph:
            graph[destination] = []
#bidirectional roads
        graph[source].append((destination, distance))
        graph[destination].append((source, distance))

    return graph

# graph = graph_rep("indian_cities_dataset.csv")
# #graph display
# for city in graph:
#     print(city, "->", graph[city])