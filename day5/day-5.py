string = open("input.txt").read()

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

print("units remaining", string.__len__())
