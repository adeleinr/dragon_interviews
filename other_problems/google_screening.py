"""
Imagine
we
own
a
parking
garage.All
day, cars
enter and exit.When
a
car
enters, it
takes
a
ticket
from the gate

machine.When
a
car
exits, it
returns
the
ticket
to
the
gate
machine.The
machine
prints
the
entry and exit
time
on
each
ticket.
2
​
3
Now, it
's the end of the day, and we'
ve
got
a
big
pile
of
tickets.We
want
to
figure
out
how
many
cars
were in the
garage
at
each
time
of
the
day.
4
​
5
Formally: Please
write
a
function
that
takes as input
an
integer
N(number
of
timesteps) and a
list
`tickets`, and returns
a
list
R
such
that
len(R) == N and R[i] == the
number
of
elements
of
`tickets`
such
that
entry <= i <= exit(i.e.both
are
inclusive).
6
​
7
Example:
8
N = 5
9
tickets = [(1, 3), (2, 4)](1, 2)
M
10
result = [0, 1, 2, 2, 1]
N
11
0 - 1, 1 - 2, 2 - 3, 3 - 4
12

13
[0, 0, 0, 0, 0]
14
​
15
[0, 1, 1, 0, 0]
16
​
17
"""


def num_cars(tickets, n):
    result = [0] * n
    for start, end in tickets:
        for i in range(start, end):
            result[i] += 1
    return result


print(num_cars([(1, 3), (2, 4)], 5))

import math


def find_station_neighbors(id, firestations, n):
    n = max(n, len(firestations))
    x, y = firestations[id]
    neighbors = []
    for curr_id, cor in firestations.items():
        if curr_id != id:
            distance = math.sqrt(math.pow((x - cor[0]), 2) + math.pow((y - cor[1]), 2))
            neighbors.append((curr_id, distance))
    neighbors = sorted(neighbors, key=lambda tup: tup[1])
    return neighbors[:n]


print(find_station_neighbors(1, {1:(1,2), 2:(2,3), 3:(4,5)}, 3))