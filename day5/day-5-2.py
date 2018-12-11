def fully_react_polymer(polymer_string):
    string = polymer_string
    current_index = 0
    while current_index < string.__len__():
        if current_index != string.__len__() - 1:
            if string[current_index].islower():
                if string[current_index + 1].isupper() and string[current_index + 1] == string[current_index].upper():
                    string = string[:current_index] + string[current_index + 2:]
                    current_index -= 2
            if string[current_index].isupper():
                if string[current_index + 1].islower() and string[current_index + 1] == string[current_index].lower():
                    string = string[:current_index] + string[current_index + 2:]
                    current_index -= 2
        current_index += 1
    return string


full_polymer = open("input.txt").read()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char_list = []

for index, letter in enumerate(alphabet):
    polymer = full_polymer.replace(letter.lower(), '')
    polymer = polymer.replace(letter.upper(), '')
    fully_reacted_polymer = fully_react_polymer(polymer)
    char_list.append([letter, fully_reacted_polymer.__len__()])

shortest_polymer = ['', 999999999]
for character in char_list:
    if character[1] < shortest_polymer[1]:
        shortest_polymer = character

print("length of the shortest polymer", shortest_polymer[1])
