from collections import defaultdict

input = open("input.txt")

graph = defaultdict(set)
unique_steps = set()

for line in input:
    split = line.split(' ')
    before = split[1]
    after = split[7]
    unique_steps.add(before)
    unique_steps.add(after)
    graph[before]
    graph[after].add(before)

alphabetical_steps = sorted(unique_steps)
order = []
i = 0

while i < alphabetical_steps.__len__():
    if graph[alphabetical_steps[i]].__len__() == 0:
        for graph_set in graph:
            if alphabetical_steps[i] in graph[graph_set]:
                graph[graph_set].remove(alphabetical_steps[i])
        del graph[alphabetical_steps[i]]
        order.append(alphabetical_steps.pop(i))
        i = 0
    else:
        i += 1

print(''.join(order))

