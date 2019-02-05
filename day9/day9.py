num_players = 459
num_marbles = 71790

player_list = {i: 0 for i in range(num_players)}

marble_circle_list = []

current_index = 0

# lots of off-by-one issues in this problem
for i in range(num_marbles + 1):
    if i % 23 == 0 and i != 0:
        prev_index = (current_index - 7) % (marble_circle_list.__len__())
        points = i + marble_circle_list.pop(prev_index)
        player_list[i % num_players] += points
        current_index = prev_index % marble_circle_list.__len__()
    else:
        if marble_circle_list.__len__() == 0:
            marble_circle_list.insert(0, i)
        else:
            current_index = ((current_index + 1) % marble_circle_list.__len__()) + 1
            marble_circle_list.insert(current_index, i)

print(max(player_list.values()))
