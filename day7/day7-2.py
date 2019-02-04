from collections import defaultdict
import re
from itertools import count as count_from


def schedule(pairs, workers=5):
    steps = {step for pair in pairs for step in pair}
    prereqs = defaultdict(list)
    for pair in pairs:
        prereqs[pair[1]].append(pair[0])
    endtimes = {step: infinity for step in steps}
    for t in count_from(0):
        def available_steps(step):
            for p in prereqs[step]:
                if endtimes[p] >= t:
                    return False
            return True
        available = filter(available_steps, steps)
        for step in sorted(available)[:workers]:
            endtimes[step] = t + 60 + ord(step) - ord('A')
            steps.remove(step)
            workers -= 1
        for step in endtimes:
            if endtimes[step] == t:
                workers += 1
        if not steps:
            return endtimes


input = open("input.txt")

infinity = float('inf')

pairs = []

for line in input:
    split = line.split(' ')
    before = split[1]
    after = split[7]
    pairs.append([before, after])

print(max(schedule(pairs).values()) + 1)
