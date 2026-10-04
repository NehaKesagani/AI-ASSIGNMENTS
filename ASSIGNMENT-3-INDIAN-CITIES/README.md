### Problem Statement
When actions have different costs in a state based search space, an obvious choice is to use best-first search where the evaluation function is the cost of the path from the root to the current node. This is called Dijkstra’s algorithm by the theoretical computer science community, and uniform-cost search Uniform-cost search by the AI community. Implement the Dijkstra’s algorithm to all the cities in India and their Road distances. This info may be taken from open sources.
## Objective
To find and calculate the shortest path between any two given available cities.

## Dataset
The dataset contains road distance between Indian cities.
- 20 cities
- 51 road connections
- Bidirectional roads

### Cities

1. Agra
2. Ahmedabad
3. Bengaluru
4. Bhubaneswar
5. Chennai
6. Delhi
7. Goa
8. Hyderabad
9. Jaipur
10. Kanpur
11. Kochi
12. Kolkata
13. Lucknow
14. Mumbai
15. Patna
16. Pune
17. Thiruvananthapuram
18. Udaipur
19. Varanasi
20. Vishakhapatnam

## Dataset Source

The road distance information was obtained from publicly available open source data containing distances between Indian cities.

### Sample Output
(venv) PS C:\Users\Neha Kesagani\Desktop\SEM 1\EOAI\Assignemts\ASSIGNMENT-3 INDIAN CITIES> python main.py

Available Cities:
- Agra
- Ahmedabad
- Bengaluru
- Bhubaneswar
- Chennai
- Delhi
- Goa
- Hyderabad
- Jaipur
- Kanpur
- Kochi
- Kolkata
- Lucknow
- Mumbai
- Patna
- Pune
- Thiruvananthapuram
- Udaipur
- Varanasi
- Vishakhapatnam

Enter source city: Agra
Enter destination city: Thiruvananthapuram

Source      : Agra
Destination : Thiruvananthapuram

Shortest Path:
Agra → Delhi → Jaipur → Pune → Goa → Kochi → Thiruvananthapuram

Total Distance: 3141 km
(venv) PS C:\Users\Neha Kesagani\Desktop\SEM 1\EOAI\Assignemts\ASSIGNMENT-3 INDIAN CITIES> 