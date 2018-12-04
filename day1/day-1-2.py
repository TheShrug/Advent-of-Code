frequenciesList = []
frequency = 0
duplicateFrequency = 0

while duplicateFrequency == 0:
    file = open("input.txt")
    for line in file:
        frequency += int(line)
        if frequency in frequenciesList:
            duplicateFrequency = frequency
            break
        frequenciesList.append(frequency)

print("First duplicated frequency: ", duplicateFrequency)