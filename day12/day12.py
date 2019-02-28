import collections
from recordtype import recordtype
import matplotlib.pyplot as plt


def place_empty_pots_around(pots):
    first_pot_number = pots[0].number
    last_pot_number = pots[-1].number
    for i in range(5):
        if pots[i].value == '#':
            for pot_index in range(5 - (i)):
                pots.appendleft(Pot(first_pot_number - (pot_index + 1), '.'))
            break
    for i in range(5):
        if pots[-i - 1].value == '#':
            for pot_index in range(5 - i):
                pots.append(Pot(last_pot_number + (pot_index + 1), '.'))
            break
    return pots


def simulate_day(pots, rules):
    pots = place_empty_pots_around(pots)
    # we check for all the patterns for the day, then after the day is complete, execute the changes to the pots
    # we'll store the number of the pot and the new value in a list
    changed_pot_deque = collections.deque()
    for index, pot in enumerate(pots):
        changed_pot_deque.append(check_pot_for_pattern(index, pot, pots, rules))

    return changed_pot_deque


def simulate_days(number_of_days, pots, rules):
    count_at_each_generation = []
    for i in range(number_of_days):
        pots = simulate_day(pots, rules)
        count_at_each_generation.append(get_count(pots))
    return count_at_each_generation


def check_pot_for_pattern(index, pot, pots, rules):
    first_pot_number = pots[0].number
    last_pot_number = pots[-1].number
    if last_pot_number - 1 > pot.number > first_pot_number + 1:
        pot_pattern = []
        for i in range(5):
            pot_pattern.append(pots[(index - 2) + i].value)
        for rule in rules:
            if pot_pattern == rule.pattern:
                return Pot(pot.number, rule.output)
    return pot


def get_count(pots):
    count = 0
    for pot in pots:
        if pot.value == '#':
            count += pot.number
    return count


input = open("input.txt")

Rule = collections.namedtuple('Rule', 'pattern, output')
Pot = recordtype('Pot', 'number, value')

rules = []
pots = collections.deque()

for index, line in enumerate(input):
    if index == 0:
        for char_index, char in enumerate(line[15:].rstrip()):
            pots.append(Pot(char_index, char))
    if index > 1:
        pattern = []
        for char in line[0:5]:
            pattern.append(char)
        rules.append(Rule(pattern, line[9]))


final_counts = simulate_days(800, pots, rules)

"""
simulating 50 billion days was not reasonable with this algorithm. The better approach would be to try and 
find a pattern and calculate from that. Turns out at less than 200 generations the number
starts increasing by 42 per generation. matplotlib is pretty neat
"""

plt.plot(final_counts)
plt.show()

print(final_counts[-1] + (42 * 49999999800))

