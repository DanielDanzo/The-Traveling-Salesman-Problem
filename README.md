# The-Traveling-Salesman-Problem

Based on the famous traveling saleman problem. The problem states that: "A salesman has to visit different cities as part of his job, and still return to his origin city. You are requested to determine the shortest(or optimal) path that can be taken by the salesman.". Presented is a solution that uses a greedy Hamiltonian approach to the problem. Each node is visited exactly once, then in each visit,  the nearest city that has not been visited  is the next city to be visited. This is not the most optimal solution but it is a close approximation to the most optimal solution.

## Running the program

The program takes as input the number of cities that are to be visited. The cities are then randomly generated on a canvas, then the shortest path is then found. The blue node represents the starting city and the blue vertex represents the first route taken to the first city. The program is run as follows:

```bash
python salesperson.py {number of cities}
```

### Example

```bash
python salesperson.py 30
```

The program will randomly generate 30 cities to be visited. Then the greedy Hamiltonian algorithm is run to find the shortest path.
A canvas will be displayed showing the path taken.
